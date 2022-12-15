from selenium.webdriver.support.wait import WebDriverWait
from pages.base_app import BasePage
from selenium.webdriver.common.by import By


class OrderFirstPage(BasePage):
    """Создали класс, в котором будут храниться все локаторы , необходимые для проверки регистрации"""

    # локатор строки "Имя"
    NAMELINE = [By.XPATH, "//input[@placeholder='* Имя']"]
    # локатор строки "Фамилия"
    LASTNAMELINE = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    # локатор строки "Адрес"
    ADRESSLINE = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    # локатор строки "Метро"
    SUBWAYSTATION = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    # локатор строки "Телефон"
    PHONENUMBER = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    # локатор кнопки "Далее"
    NEXT = [By.XPATH, "//button[text()='Далее']"]
    #локатор значения в выпадающем списке
    CHOICE = [By.CLASS_NAME, "select-search__row"]
    #локатор кнопки Куки
    COOKIE = [By.XPATH, "//button[@class='App_CookieButton__3cvqF']"]


    # #метод нажатия на первую строку
    # def first_line_click(self):
    #     name = self.find_element(OrderFirstPage.NAMELINE, time=10)
    #     self.click_element(name)

    #метод  передачи данных в первую строку
    def first_line_send_data(self, data):
        name = self.find_element(OrderFirstPage.NAMELINE, time=10)
        name.send_keys(data)

    # # метод нажатия на вторую строку
    # def second_line_click(self):
    #     lastname = self.find_element(OrderFirstPage.LASTNAMELINE, time=10)
    #     self.click_element(lastname)

    # метод  передачи данных во вторую строку
    def second_line_send_data(self, data):
        lastname = self.find_element(OrderFirstPage.LASTNAMELINE, time=10)
        lastname.send_keys(data)

    # #метод нажатия на третью строку
    # def third_line_click(self):
    #     adress = self.find_element(OrderFirstPage.ADRESSLINE, time=10)
    #     self.click_element(adress)

    # метод  передачи данных в третью строку
    def third_line_send_data(self, data):
        adress = self.find_element(OrderFirstPage.ADRESSLINE, time=10)
        adress.send_keys(data)

    #метод нажатия на выпадающий список
    def line_station_click(self):
        station = self.find_element(OrderFirstPage.SUBWAYSTATION)
        station.click()
        choice = self.find_element(OrderFirstPage.CHOICE)
        choice.click()

    # #метод нажатия на строку номера
    # def phone_number_line_click(self):
    #     number = self.find_element(OrderFirstPage.PHONENUMBER)
    #     self.click_element(number)

    #метод передачи данных в строку номера
    def phone_number_line_send_data(self, data):
        number_line = self.find_element(OrderFirstPage.PHONENUMBER)
        number_line.send_keys(data)

    #метод нажатия на кнопку далее
    def button_next_click(self):
        button = self.find_element(OrderFirstPage.NEXT)
        button.click()

    # #метод скролла до строки выпадающего списка
    # def line_list_scroll(self):
    #     station = self.find_element(OrderFirstPage.SUBWAYSTATION)
    #     self.scroll_to_element(station)

    # #метод принятия Куки
    # def cookie_accept(self):
    #     cookie_button = self.find_element(OrderFirstPage.COOKIE)
    #     self.click_element(cookie_button)

    # #метод скролла до кнопки Далее
    # def button_next_scroll(self):
    #     button_next = self.find_element(OrderFirstPage.NEXT)
    #     self.scroll_to_element(button_next)


