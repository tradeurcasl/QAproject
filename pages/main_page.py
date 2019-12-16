
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .login_page import LoginPage

class MainPage(BasePage):
    def go_to_login_page(self):
            link = self.browser.find_element(By.CSS_SELECTOR, '#login_link')
            link.click()
    def should_be_login_link(self):
        self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
