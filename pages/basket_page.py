import time
from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def see_product_in_basket_opened_from_product_page(self, browser):
        self.browser = browser
        link = self.browser.find_element(*BasePageLocators.CART_LINK)
        link.click()
        time.sleep(3)
        assert self.is_element_present(*BasePageLocators.CART_EMPTY), 'Cart is not empty'
