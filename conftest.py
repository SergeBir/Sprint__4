import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    driver = webdriver.Chrome(executable_path='/Users/sergeibiryukov/yandex/Sprint__4/chromedriver')
    yield driver
    driver.quit()
    