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

class PageObjectLocators():
    ADD = [By.XPATH, '//*[@id="add_to_basket_form"]/button']

