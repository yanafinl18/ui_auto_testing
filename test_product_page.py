import time

from .pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize("promo_code", ["0", "1", "2", "3", "4", "5", "6",
                                        pytest.param("7", marks=pytest.mark.xfail),
                                        "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_code):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{}".format(promo_code)
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()


@pytest.mark.skip()
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    assert page.should_not_be_success_message(), "Сообщение о добавлении в корзину повилось"


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    assert page.should_not_be_success_message(), "Сообщение о добавлении в корзину повилось"


@pytest.mark.skip()
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    assert page.should_success_message_disappeared(), "Не пропало сообщение"
