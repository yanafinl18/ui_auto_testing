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

