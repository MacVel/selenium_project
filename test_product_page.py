import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.product_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = [
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
]


@pytest.mark.parametrize('link', url) 
def test_adding_in_basket(browser,link):
    page = ProductPage(browser,link)
    page.open()
    page.add_to_basket()
    page.should_be_successfully_add_to_baskets()
    page.should_basket_price_equal_product_price()



@pytest.mark.parametrize('link', url) 
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser,link):
    page = ProductPage(browser,link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.parametrize('link', url) 
def test_guest_cant_see_success_message(browser,link):
    page=ProductPage(browser,link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.parametrize('link', url) 
def test_message_disappeared_after_adding_product_to_basket(browser,link):
    page=ProductPage(browser,link)
    page.open()
    page.add_to_basket()
    page.should_message_is_disappeared()

@pytest.mark.parametrize('link', url) 
def test_guest_should_see_login_link_on_product_page(browser,link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.parametrize('link', url[2:3]) 
def test_guest_can_go_to_login_page_from_product_page(browser,link):
    page=ProductPage(browser,link)
    page.open()
    page.go_to_login_page()

@pytest.mark.smoke
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = BasketPage(browser,link)
    page.open()
    page.go_to_basket()
    page.should_not_product_in_basket()
    page.should_message_basket_is_empty()