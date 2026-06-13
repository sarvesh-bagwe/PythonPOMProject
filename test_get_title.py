import pytest
from selenium import webdriver
import time
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_get_title():
    driver = webdriver.Chrome()

    driver.get("https://google.com")
    driver.maximize_window()
    driver.implicitly_wait(2)

    time.sleep(2)
    driver.quit()



