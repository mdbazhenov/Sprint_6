from urllib.error import URLError
import pytest
from selenium import webdriver
from data import Url


@pytest.fixture
def driver():
    ff_options = webdriver.FirefoxOptions()
    ff_options.add_argument('--headless')
    driver = webdriver.Firefox()
    driver.get(Url.URL_SAMOKAT)
    yield driver
    driver.quit()



