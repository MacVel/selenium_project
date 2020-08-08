from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR,"#login_link")
  
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR,"#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR,"#register_form")
    INPUT_EMAIL = (By.CSS_SELECTOR,"#id_registration-email")
    INPUT_PASSWORD =(By.CSS_SELECTOR,"#id_registration-password1")
    INPUT_CONFIRM_PASSWORD = (By.CSS_SELECTOR,"#id_registration-password2")
    SUBMIT_REGISTRATION = (By.CSS_SELECTOR,'button[name="registration_submit"]')


class ProductPageLocators():
    BASCKET_BUTTON = (By.CSS_SELECTOR,'.btn-add-to-basket')
    SUCCESSFULL_MESSAGE = (By.CSS_SELECTOR, '#messages div:nth-child(1) .alertinner strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    BASCKET_PRICE = (By.CSS_SELECTOR,'#messages div:nth-child(3) .alertinner p strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR,"#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR,".btn-group  a.btn-default ")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    STATUS_MESSAGE = (By.CSS_SELECTOR,'#content_inner p')
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR,'.basket_summary')