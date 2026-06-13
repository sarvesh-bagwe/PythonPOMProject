from selenium.webdriver.common.by import By
from Utils.browser_util import BrowserUtil


class LoginPage(BrowserUtil):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username = (By.ID, 'user-name')
        self.password = (By.ID, 'password')
        self.login_button = (By.NAME, 'login-button')
        self.product_page = (By.XPATH, "//div/span[text()='Products']")


    def login(self, user, pas):
        self.driver.get("https://www.saucedemo.com/")
        print("\n",self.get_title())

        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pas)
        self.driver.find_element(*self.login_button).click()

        product_page = self.driver.find_element(*self.product_page).text
        assert product_page == "Products"

        print("Logged in Successfully")