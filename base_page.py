class BasePage():
    def __init_(self,browser,url):
        self.browser = browser
        self.url = url
    def open_url(self):
        self.browser.get(self.url)

