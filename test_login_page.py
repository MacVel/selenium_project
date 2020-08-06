from .pages.login_page import LoginPage


def test_login_form_present(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    login_page = LoginPage(browser,link)
    login_page.open()
    login_page.should_be_login_form()

def test_registration_form_present(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    login_page = LoginPage(browser,link)
    login_page.open()
    login_page.should_be_register_form()

def test_url_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    login_page = LoginPage(browser,link)
    login_page.open()
    login_page.should_be_login_url()