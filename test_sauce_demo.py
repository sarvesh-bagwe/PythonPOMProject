from PageObjects.cart_page import CartPage
from PageObjects.checkout_page import CheckoutPage
from PageObjects.login_page import LoginPage
from PageObjects.products_page import ProductPage
from Utils.logger import log_details
import json
import pytest


def load_test_data():
    with open('./TestData/test_data.json', 'r') as f:
        test_data = json.load(f)
        data_list = test_data["data"]
    return data_list

@pytest.mark.smoke
@pytest.mark.parametrize("data_list", load_test_data())
# @pytest.mark.usefixtures("setup")
class TestSauceDemo:

    def test_add_cart(self,setup,data_list):
        driver = setup
        logger = log_details()
        # print(data_list["username"])

        login = LoginPage(driver)
        login.login(data_list["username"], data_list["password"])

        driver.get_screenshot_as_file('product_page.jpg') # take screenshot
        logger.info("Login Successful")

        products = ProductPage(driver)
        products.product_selection()

        cart = CartPage(driver)
        cart.check_cart()

        checkout = CheckoutPage(driver)
        checkout.checkout(data_list["firstname"], data_list["lastname"], data_list["postalcode"])







