from .pages.product_page import ProductPage
import pytest
from .pages.product_page import ProductPage
import time
list_of_pages = a = [x for x in range(10)]

@pytest.mark.parametrize('pages', list_of_pages)
def test_guest_can_add_product_to_cart(browser, pages):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{}".format(pages)
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(2)
    page.should_be_message_basket_total()
    page.should_be_message_about_adding()