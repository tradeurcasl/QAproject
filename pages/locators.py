from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = [By.CSS_SELECTOR, '#login_link']

class LoginPageLocators():
    LOGIN_LINK = [By.CSS_SELECTOR, '#login_link']
    EMAIL_LOG = [By.CSS_SELECTOR, '#id_login-username']
    PASSWORD_LOG = [By.CSS_SELECTOR, '#id_login-password']
    BUTTON_LOG = [By.CSS_SELECTOR, 'button[name="login_submit"]']
    EMAIL_REG = [By.CSS_SELECTOR,'#id_registration-email']
    PASS_LOG1 = [By.CSS_SELECTOR, '#id_registration-password1']
    PASS_LOG2 = [By.CSS_SELECTOR, '#id_registration-password2']
    BUTTON_REG = [By.CSS_SELECTOR, 'button[name="registration_submit"']
    LOG_IN = [By.CSS_SELECTOR, '#login_form']
    REG_IN = [By.CSS_SELECTOR, '#register_form']

class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ALERT_ADDED_TO_CART = (By.CSS_SELECTOR, "div.alertinner")
    ALERT_CART_STATUS = (By.CSS_SELECTOR, ".alert-noicon.alert-info p")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner ")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
