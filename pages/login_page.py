from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        curr_url = self.browser.current_url
        assert "login" in curr_url, "Incorrect url"

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Login Form is not exist"

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTERED_FORM), "Registered Form is not exist"
