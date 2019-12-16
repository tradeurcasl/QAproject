from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import PageObjectLocators

class PageObject(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*PageObjectLocators.ADD)
        button.click()
