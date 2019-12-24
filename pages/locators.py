from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = [By.CSS_SELECTOR, "#login_link"]
    LOGIN_LINK_INVALID = [By.CSS_SELECTOR, "#login_link_inc"]
    CART_LINK=[By.CSS_SELECTOR, 'span.btn-group']
    CART_EMPTY =[By.XPATH, "//*[@id='content_inner']/p"]
    USER_ICON = [By.CSS_SELECTOR, ".icon-user"]

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
    BUTTON_ADD_TO_BASKET = [By.CSS_SELECTOR, "button.btn-add-to-basket"]
    ALERT_ADDED_TO_CART = [By.CSS_SELECTOR, "div.alertinner"]
    MESSAGE_ABOUT_ADDING = [By.CSS_SELECTOR, "div.alertinner"]
    PRODUCT_NAME = [By.CSS_SELECTOR, "div.product_main h1"]
    MESSAGE_BASKET_TOTAL = [By.CSS_SELECTOR, ".alert-info .alertinner strong"]
    PRODUCT_PRICE = [By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]"]
    SUCCESS_MESSAGE = [By.XPATH, '//div[contains(@class, "alert-success")]/div[contains(@class,"alertinner")]']