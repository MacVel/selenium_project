from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from time import sleep

class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BASCKET_BUTTON).click()
        self.solve_quiz_and_get_code()


    def should_be_successfully_add_to_baskets(self):
        name_of_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.SUCCESSFULL_MESSAGE).text
        assert name_of_product == message

    def should_basket_price_equal_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASCKET_PRICE).text
        assert product_price == basket_price
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESSFULL_MESSAGE)

    def should_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESSFULL_MESSAGE)
    

    