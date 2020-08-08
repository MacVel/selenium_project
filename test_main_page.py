import pytest
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage



def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser,link)
    page.open()
    page.go_to_login_page()

    
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser,link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser,link)
    page.open()
    page.go_to_basket()
    page.should_not_product_in_basket()
    page.should_message_basket_is_empty()