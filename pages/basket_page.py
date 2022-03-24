from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_header()

    def should_be_basket_url(self):
        curr_url = self.browser.current_url
        assert "basket" in curr_url, "Incorrect url {}".format(curr_url)

    def should_be_basket_header(self):
        basket_header = self.browser.find_element(*BasketPageLocators.BASKET_HEADER).text
        assert basket_header in ["Корзина", "Basket"], "Header is incorrect"

    def should_be_empty_basket(self):
        basket = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET).text
        assert basket in ["Your basket is empty", "Ваша корзина пуста"], "Basket is not empty"
