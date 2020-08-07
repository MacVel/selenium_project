import math
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException,NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators

class BasePage():
    def __init__(self,browser, url,timeout=10):
        self.browser = browser
        self.url = url
        #self.browser.implicitly_wait(timeout)
    def open(self):
        self.browser.get(self.url)

    def is_element_present(self,how,what):
        try:
            self.browser.find_element(how,what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self,how,what,timeout=4):
        try:
            WebDriverWait(self.browser,timeout).until(EC.presence_of_element_located((how,what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self,how,what,timeout=4):
        try:
            WebDriverWait(self.browser,timeout).until_not(EC.presence_of_element_located((how,what)))
        except TimeoutException:
            return False
        return true

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_basket(self):
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link .click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "login link is not presented"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = int(alert.text.split(sep=' ')[2])
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        self.browser.implicitly_wait(10)
        try:
            self.browser.implicitly_wait(10)
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
        
    

    