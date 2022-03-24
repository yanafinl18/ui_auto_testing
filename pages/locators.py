from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-group .btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTERED_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    LOGIN_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    LOGIN_REPEAT_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")
    SUCCESS_REGISTRATION = (By.CSS_SELECTOR, ".alertinner.wicon")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_ADD_SUCCESS = (By.CSS_SELECTOR, ".alertinner")
    BOOK_NAME = (By.CSS_SELECTOR, ".breadcrumb .active")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#messages div:nth-child(1) div strong")
    BASKET_LINK_FROM_PRODUCT = (By.TAG_NAME, "a")


class BasketPageLocators():
    BASKET_HEADER = (By.CSS_SELECTOR, ".page-header h1")
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")
