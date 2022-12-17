import pytest
from pages.home_page import MainHomePage
from pages.first_page_of_order import OrderFirstPage
from pages.second_page_of_order import OrderSecondPage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# проверка заказа через верхнюю кнопку
def test_make_order_through_upper_button_true(browser):
    home = MainHomePage(browser)
    order = OrderFirstPage(browser)
    second_page = OrderSecondPage(browser)
    home.go_to_site()
    WebDriverWait(browser, 3).until(
        expected_conditions.element_to_be_clickable(MainHomePage.ACCEPTCOOKIE))
    home.cookies_accept()
    home.upper_order_click()
    WebDriverWait(browser, 3).until(
        expected_conditions.presence_of_element_located(OrderFirstPage.NAMELINE))
    order.all_lines_send_data("Сергей", "Бирюков", "Москва")
    order.moving_to_second_page("89999999999")
    second_page.first_line_click_with_choice()
    second_page.first_line_send_data("17.12.2022")
    second_page.choice_all_rest_elements("Пишу свой первый автотест!")
    second_page.button_order_click()
    second_page.confirm_button_click()
    message = second_page.search_text_after_confirm()
    assert "Заказ оформлен" in message.text

# проверка заказа через нижнюю кнопку
def test_make_order_through_lower_button_true(browser):
    home = MainHomePage(browser)
    order = OrderFirstPage(browser)
    second_page = OrderSecondPage(browser)
    home.go_to_site()
    WebDriverWait(browser, 3).until(
        expected_conditions.element_to_be_clickable(MainHomePage.ACCEPTCOOKIE))
    home.cookies_accept()
    home.lower_order_click()
    WebDriverWait(browser, 3).until(
        expected_conditions.presence_of_element_located(OrderFirstPage.NAMELINE))
    order.all_lines_send_data("Сергей", "Бирюков", "Смоленск")
    order.moving_to_second_page("89888888888")
    second_page.first_line_click_with_choice()
    second_page.first_line_send_data("17.12.2022")
    second_page.choice_all_rest_elements("Пишу свой второй автотест!")
    second_page.button_order_click()
    second_page.confirm_button_click()
    message = second_page.search_text_after_confirm()
    assert "Заказ оформлен" in message.text
