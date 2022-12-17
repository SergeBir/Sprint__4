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

    #метод  передачи данных в первую строку
    def first_line_send_data(self, firstname):
        name = self.find_element(OrderFirstPage.NAMELINE, time=10)
        name.send_keys(firstname)

    # метод  передачи данных во вторую строку
    def second_line_send_data(self, surname):
        lastname = self.find_element(OrderFirstPage.LASTNAMELINE, time=10)
        lastname.send_keys(surname)

    # метод  передачи данных в третью строку
    def third_line_send_data(self, place):
        adress = self.find_element(OrderFirstPage.ADRESSLINE, time=10)
        adress.send_keys(place)

    # метод заполнения всех строк клиента
    def all_lines_send_data(self,name, lastname, adress):
        self.first_line_send_data(name)
        self.second_line_send_data(lastname)
        self.third_line_send_data(adress)


    # метод нажатия на выпадающий список
    def line_station_click(self):
        station = self.find_element(OrderFirstPage.SUBWAYSTATION)
        station.click()
        choice = self.find_element(OrderFirstPage.CHOICE)
        choice.click()

    #метод передачи данных в строку номера
    def phone_number_line_send_data(self, data):
        number_line = self.find_element(OrderFirstPage.PHONENUMBER)
        number_line.send_keys(data)

    #метод нажатия на кнопку далее
    def button_next_click(self):
        button = self.find_element(OrderFirstPage.NEXT)
        button.click()

    # метод выбора в списке, передача номера телефона и перехода на вторую вкладку
    def moving_to_second_page(self, phone_number):
        self.line_station_click()
        self.phone_number_line_send_data(phone_number)
        self.button_next_click()


