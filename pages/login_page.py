from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import faker


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'There is no login in url'

    def should_be_login_form(self):
        self.browser.find_element(*LoginPageLocators.LOG_IN)
        assert True, "There is no login form"

    def should_be_register_form(self):
        self.browser.find_element(*LoginPageLocators.REG_IN)
        assert True, 'There is no registration form'

    def register_new_user(self, email, password):
        input1 = self.browser.find_element(*LoginPageLocators.EMAIL_REG)
        input1.send_keys(email)
        input2 = self.browser.find_element(*LoginPageLocators.PASS_LOG1)
        input2.send_keys(password)
        input3 = self.browser.find_element(*LoginPageLocators.PASS_LOG2)
        input3.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.BUTTON_REG)
        button.click()
