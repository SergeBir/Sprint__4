import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    driver = webdriver.Firefox(executable_path='/Users/sergeibiryukov/yandex/Sprint__4/geckodriver')
    yield driver
    driver.quit()
    