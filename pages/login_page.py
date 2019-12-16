from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        str = self.browser.current_url()
        assert str==str.find("login"), 'There is no login in url'

    def should_be_login_form(self):
        form = self.browser.find_element(LoginPageLocators.LOG_IN)
        assert True, "There is no login form"

    def should_be_register_form(self):
        fom = self.browser.find_element(LoginPageLocators.REG_IN)
        assert True, 'There is no registration form'