import pytest
import time
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.product_page import BasePage
from .pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



product_page = ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/",]


@pytest.mark.review
@pytest.mark.parametrize('link', product_page) 
def test_guest_can_add_product_to_basket(browser,link):
    page = ProductPage(browser,link)
    page.open()
    page.add_to_basket()
    page.should_be_successfully_add_to_baskets()
    page.should_basket_price_equal_product_price()


@pytest.mark.xfail
@pytest.mark.parametrize('link', product_page) 
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser,link):
    page = ProductPage(browser,link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.parametrize('link', product_page) 
def test_guest_cant_see_success_message(browser,link):
    page=ProductPage(browser,link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
@pytest.mark.parametrize('link', product_page) 
def test_message_disappeared_after_adding_product_to_basket(browser,link):
    page=ProductPage(browser,link)
    page.open()
    page.add_to_basket()
    page.should_message_is_disappeared()


@pytest.mark.parametrize('link',product_page) 
def test_guest_should_see_login_link_on_product_page(browser,link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.review
@pytest.mark.parametrize('link', product_page) 
def test_guest_can_go_to_login_page_from_product_page(browser,link):
    page=ProductPage(browser,link)
    page.open()
    page.go_to_login_page()


@pytest.mark.review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = BasketPage(browser,link)
    page.open()
    page.go_to_basket()
    page.should_not_product_in_basket()
    page.should_message_basket_is_empty()


@pytest.mark.authorization_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function',autouse=True)
    def setup(self,browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        email = str(time.time()) + "@fakemail.org"
        page=LoginPage(browser,link)
        page.open()
        page.register_new_user(email,'JS242sfK21ksdw')
        page.should_be_authorized_user()

    
    def test_user_cant_see_success_message(self,browser):
        link = product_page[0]
        page=ProductPage(browser,link)
        page.open()
        page.should_not_be_success_message()


    @pytest.mark.review
    def test_user_can_add_product_in_basket(self,browser):
        link = product_page[0]
        page = ProductPage(browser,link)
        page.open()
        page.add_to_basket()
        page.should_be_successfully_add_to_baskets()
        page.should_basket_price_equal_product_price()
