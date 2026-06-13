from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrom", help="Browser selection"
    )

@pytest.fixture()
def setup(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()

    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(params=[('Sarvesh', 'Bagwe', 5.8),('Tanika', 'Garg', 5.4)])
def param_loader(request):
    return request.param

