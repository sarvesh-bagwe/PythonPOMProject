from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utils.browser_util import BrowserUtil


class CartPage(BrowserUtil):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.cart_page_title = (By.CLASS_NAME, 'title')
        self.cart_item = (By.CLASS_NAME, 'cart_item')
        self.checkout_button = (By.ID, 'checkout')


    def check_cart(self):
        cart_page = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.cart_page_title))

        assert cart_page.text == "Your Cart", "Cart page not loaded correctly"

        cart_item = self.driver.find_element(*self.cart_item).is_displayed()

        assert cart_item, "Cart item was not displayed, cannot proceed to checkout"

        self.driver.find_element(*self.checkout_button).click()

        print("Cart Verified")