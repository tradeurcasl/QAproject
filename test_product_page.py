from .pages.product_page import ProductPage
from .pages.base_page import BasePage
import pytest
import time
list_of_pages = a = [0, 1,
                     pytest.param(7, marks=pytest.mark.xfail),
                     ]
@pytest.mark.skip
def test_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.see_success_message_after_adding_product_to_basket()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.guest_cant_see_success_message()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    time.sleep(1)
    page.message_disappeared_after_adding_product_to_basket()

@pytest.mark.parametrize('pages', list_of_pages)
def test_guest_can_add_product_to_cart(browser, pages):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{}".format(pages)
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(4)
    page.should_be_message_basket_total()
    page.should_be_message_about_adding()
