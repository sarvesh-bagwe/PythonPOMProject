import time

from  selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utils.browser_util import BrowserUtil


class ProductPage(BrowserUtil):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.product_page = (By.CLASS_NAME, 'title')
        self.item = (By.XPATH, "//div[text()='Sauce Labs Backpack']")
        self.item_add_button = (By.XPATH, "//div[contains(text(),'Backpack')]//" \
                                      "ancestor::div[contains(@class,'inventory_item_description')]//child::button")
        self.item_count = (By.XPATH, "//span[@class='shopping_cart_badge']")
        self.shopping_cart = (By.CLASS_NAME, 'shopping_cart_link')


    def product_selection(self):

        print(self.get_title())

        product_page = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.product_page))

        assert product_page.text == "Products", "Cart page not loaded correctly"

        assert self.driver.find_element(*self.item).is_displayed()
        time.sleep(5)
        self.driver.find_element(*self.item_add_button).click()
        time.sleep(5)

        item_count = self.driver.find_element(*self.item_count).text
        assert item_count == '1', 'Cart item count does not match'

        self.driver.find_element(*self.shopping_cart).click()

        print("Product Selection Done Successfully")




