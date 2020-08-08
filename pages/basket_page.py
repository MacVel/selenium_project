from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET)

    def should_message_basket_is_empty(self):
        if self.should_not_product_in_basket():
            user_language = self.browser.execute_script("return window.navigator.userLanguage || window.navigator.language")
            message = self.browser.find_element(By.CSS_SELECTOR,BasketPageLocators.STATUS_MESSAGE).text
            assert languages[user_language] in message
        else:
            return False