import time

from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        book_name = self.should_be_book_name()
        self.add_product_to_basket()
        self.solve_quiz_and_get_code()
        time.sleep(5)
        self.should_be_alert()
        book_name_in_basket = self.should_be_book_name_in_basket()
        # time.sleep(90)
        assert book_name == book_name_in_basket, "Не совпали имена книг в корзине и при заказе"

    def add_product_to_basket(self):
        add_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_btn.click()

    def should_be_alert(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_SUCCESS), "Товар не добавлен в корзину"

    def should_be_book_name(self):
        book = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        return str(book)

    def should_be_book_name_in_basket(self):
        book_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return str(book_in_basket)
