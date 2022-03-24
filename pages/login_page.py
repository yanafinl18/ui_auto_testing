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

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        pass_first_fiels = self.browser.find_element(*LoginPageLocators.LOGIN_FIELD)
        pass_first_fiels.send_keys(password)
        pass_second_fiels = self.browser.find_element(*LoginPageLocators.LOGIN_REPEAT_FIELD)
        pass_second_fiels.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()

    def success_registration_message(self):
        registration_text = self.browser.find_element(*LoginPageLocators.SUCCESS_REGISTRATION)
        assert "Спасибо за регистрацию!" in registration_text.text, "User can not to registered"
