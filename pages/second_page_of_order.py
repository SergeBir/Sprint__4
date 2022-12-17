from pages.base_app import BasePage
from selenium.webdriver.common.by import By


class OrderSecondPage(BasePage):
    """Создали класс, в котором будут храниться все локаторы , необходимые для проверки регистрации"""

    # локатор строки "Когда привезти самокат".
    DAYORDER = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    # локатор строки Время.
    TIMELINE = [By.XPATH, "//div[@class='Dropdown-placeholder']"]
    # # локатор строки "Срок аренды"
    # TIMEUSING = [By.XPATH, "//div[@class='Dropdown-control']"]
    # локатор элемента срока аренды.
    TIMEOFRESERVED = [By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']"]
    # локатор чекбокса "Цвет самоката".
    COLOR = [By.XPATH, "//input[@id = 'black'and@class='Checkbox_Input__14A2w']"]
    # локатор "Комментарий для курьера".
    COMMENT = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]
    # локатор нижней кнопки "Заказать".
    LOWERORDER = [By.XPATH, "//button[text()='Заказать' and @class='Button_Button__ra12g Button_Middle__1CSJM']"]
    # локатор верхней кнопки "Заказать".
    UPPERORDER = [By.XPATH, "//button[text()='Заказать' and @class='Button_Button__ra12g']"]
    # локатор элемента при выборе даты.
    DAYELEMENT = [By.XPATH, "//div[@role='button' and text()='17']"]
    # локатор кнопки подтверждения.
    BUTTONCONFIRM = [By.XPATH, "//button[text()='Да']"]
    # локатор строки "Успешного заказа".
    ORDERTEXT = [By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ"]']

    # метод нажатия на первую строку с выбором даты.
    def first_line_click_with_choice(self):
        day = self.find_element(OrderSecondPage.DAYORDER)
        self.click_element(day)

    # методы передачи данных в строку даты.
    def first_line_send_data(self, data):
        day = self.find_element(OrderSecondPage.DAYORDER)
        day.send_keys(data)
        element = self.find_element(OrderSecondPage.DAYELEMENT)
        self.click_element(element)

    # метод нажатия на строку времени.
    def time_line_click(self):
        time_line = self.find_element(OrderSecondPage.TIMELINE)
        time_line.click()

    # метод выбора строки из списка срока аренды.
    def time_of_reserved_choice(self):
        reserved = self.find_element(OrderSecondPage.TIMEOFRESERVED)
        reserved.click()

    # метод выбора чекбокса.
    def checkbox_click(self):
        checkbox = self.find_element(OrderSecondPage.COLOR)
        self.click_element(checkbox)

    # методы передачи текста в строку комментария.
    def comment_line_send_data(self, data):
        comment = self.find_element(OrderSecondPage.COMMENT)
        comment.send_keys(data)

    # метод нажатия на кнопку "Заказать".
    def button_order_click(self):
        button = self.find_element(OrderSecondPage.LOWERORDER)
        self.click_element(button)

    # метод нажатия на кнопку подтверждения.
    def confirm_button_click(self):
        confirm_button = self.find_element(OrderSecondPage.BUTTONCONFIRM)
        self.click_element(confirm_button)

    #метод нахождения текста подтверждения после нажатия
    def search_text_after_confirm(self):
        order_accept = self.find_element(OrderSecondPage.ORDERTEXT)
        return order_accept

    # метод заполнения всех элементов
    def all_rest_elements_choice(self, comment):
        self.checkbox_click()
        self.time_line_click()
        self.time_of_reserved_choice()
        self.comment_line_send_data(comment)
