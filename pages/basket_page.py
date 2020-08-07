from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET)
    def should_message_basket_is_empty(self):
        if self.should_not_product_in_basket():
            assert not self.is_not_element_present(*BasketPageLocators.STATUS_MESSAGE)
        else:
            return False