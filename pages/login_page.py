from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.keys import Keys

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"

    def register_new_user(self,email,password):
        self.browser.find_element(*LoginPageLocators.INPUT_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.INPUT_CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.SUBMIT_REGISTRATION).click()
    
