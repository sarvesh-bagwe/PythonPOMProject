import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utils.browser_util import BrowserUtil


class CheckoutPage(BrowserUtil):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.checkout_page_title = (By.CLASS_NAME, 'title')
        self.first_name = (By.ID, 'first-name')
        self.last_name = (By.ID, 'last-name')
        self.postal_code = (By.ID, 'postal-code')
        self.continue_button = (By.ID, 'continue')
        self.finish_button = (By.ID, 'finish')

    def checkout(self, name, lstname, pin):
        checkout_page = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.checkout_page_title))
        assert checkout_page.text == "Checkout: Your Information", "Checkout page not loaded correctly"

        self.driver.find_element(*self.first_name).send_keys(name)
        self.driver.find_element(*self.last_name).send_keys(lstname)
        self.driver.find_element(*self.postal_code).send_keys(pin)
        self.driver.find_element(*self.continue_button).click()

        time.sleep(3)
        self.driver.find_element(*self.finish_button).click()

        print("Shopping Done")
