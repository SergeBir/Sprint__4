from pages.home_page import MainHomePage
from pages.first_page_of_order import OrderFirstPage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


#проверка заказа через верхнюю кнопку
def test_make_order_through_upper_button_true(browser):
    home = MainHomePage(browser)
    order = OrderFirstPage(browser)
    home.go_to_site()
    WebDriverWait(browser, 3).until(
        expected_conditions.element_to_be_clickable(MainHomePage.ACCEPTCOOKIE))
    home.cookies_accept()
    home.upper_order_click()
    WebDriverWait(browser, 3).until(
        expected_conditions.presence_of_element_located(OrderFirstPage.NAMELINE))
    order.first_line_send_data("Сергей")
    order.second_line_send_data("Бирюков")
    order.third_line_send_data("Москва")
    order.line_station_click()
    order.phone_number_line_send_data("89999999999")
    order.button_next_click()



