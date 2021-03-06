from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        book_name = self.should_be_book_name()
        self.add_product_to_basket()
        self.solve_quiz_and_get_code()
        self.should_be_alert()
        book_name_in_basket = self.should_be_book_name_in_basket()
        assert book_name == book_name_in_basket, "Book name in the basket and in the order does not match"

    def add_product_to_basket(self):
        add_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_btn.click()

    def should_be_alert(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_SUCCESS), "The product did not add in basket"

    def should_be_book_name(self):
        book = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        return str(book)

    def should_be_book_name_in_basket(self):
        book_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return str(book_in_basket)

    def should_not_be_success_message(self):
        return self.is_not_element_present(*ProductPageLocators.PRODUCT_ADD_SUCCESS)

    def should_success_message_disappeared(self):
        return self.is_disappeared(*ProductPageLocators.PRODUCT_ADD_SUCCESS)
