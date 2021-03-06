from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import faker
import time
list_of_pages = a = [0, 1, 2, 3, 4, 5, 6,
                     pytest.param(7, marks=pytest.mark.xfail),
                     8, 9]
@pytest.mark.skip
def test_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.see_success_message_after_adding_product_to_basket()
@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(4)
    page.should_be_login_link()
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


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

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
    time.sleep(4)
    page.should_be_message_basket_total()
    page.should_be_message_about_adding()
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = BasePage(browser, link)
    page.open()
    time.sleep(2)
    page.go_to_cart(browser)
    page = BasketPage(browser, link)
    page.see_product_in_basket_opened_from_product_page()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link='http://selenium1py.pythonanywhere.com'
        page = LoginPage(browser, link)
        page.open()
        time.sleep(2)
        page.go_to_login_page()
        f = faker.Faker()
        email = f.email()
        password='viviyip87'
        page.register_new_user(email, password)
        time.sleep(2)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.guest_cant_see_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.press_button_add_to_basket()
        time.sleep(4)
        page.should_be_message_basket_total()
        page.should_be_message_about_adding()