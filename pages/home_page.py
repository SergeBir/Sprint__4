from selenium.webdriver.support.wait import WebDriverWait
from pages.base_app import BasePage
from selenium.webdriver.common.by import By


class MainHomePage(BasePage):
    """Создали класс, в котором будут храниться все локаторы , необходимые для проверки регистрации"""

    #локатор верхней кнопки "Заказать."
    UPPERORDER = [By.XPATH, "//button[@class='Button_Button__ra12g']"]
    # локатор нижней кнопки "Заказать."
    LOWERORDER = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    # локатор поля "Вопросы о важном"
    IMPORTANT = [By.XPATH, "//div[text()='Вопросы о важном']"]
    # локатор первой строки выпадающего списка
    ONELINE = [By.XPATH, "//div[@id='accordion__heading-0']"]
    # локатор текста, после нажатия на первую строку
    ONELINETEXT = [By.XPATH, "//div[@id='accordion__panel-0']//p"]
    # локатор второй строки выпадающего списка
    TWOLINE = [By.XPATH, "//div[@id='accordion__heading-1']"]
    # локатор текста, после нажатия на вторую строку
    TWOLINETEXT = [By.XPATH, "//div[@id='accordion__panel-1']//p"]
    # локатор третьей строки выпадающего списка
    THREELINE = [By.XPATH, "//div[@id='accordion__heading-2']"]
    # локатор текста, после нажатия на третью строку
    THREELINETEXT = [By.XPATH, "//div[@id='accordion__panel-2']//p"]
    # локатор четвертой строки выпадающего списка
    FOURLINE = [By.XPATH, "//div[@id='accordion__heading-3']"]
    # локатор текста, после нажатия на четвертую строку
    FOURLINETEXT = [By.XPATH, "//div[@id='accordion__panel-3']//p"]
    # локатор пятой строки выпадающего списка
    FIVELINE = [By.XPATH, "//div[@id='accordion__heading-4']"]
    # локатор текста, после нажатия на пятую строку
    FIVELINETEXT = [By.XPATH, "//div[@id='accordion__panel-4']//p"]
    # локатор шестой строки выпадающего списка
    SIXLINE = [By.XPATH, "//div[@id='accordion__heading-5']"]
    # локатор текста, после нажатия на шестую строку
    SIXLINETEXT = [By.XPATH, "//div[@id='accordion__panel-5']//p"]
    # локатор седьмой строки выпадающего списка
    SEVENLINE = [By.XPATH, "//div[@id='accordion__heading-6']"]
    # локатор текста, после нажатия на седьмую строку
    SEVENLINETEXT = [By.ID, "accordion__panel-6"]
    # локатор восьмой строки выпадающего списка
    EIGHTLINE = [By.XPATH, "//div[@id='accordion__heading-7']"]
    # локатор текста, после нажатия на восьмую строку
    EIGHTLINETEXT = [By.XPATH, "//div[@id='accordion__panel-7']//p"]
    #локатор Cookie
    ACCEPTCOOKIE = [By.XPATH, '//button[@class="App_CookieButton__3cvqF"]']
    #локатор логотипа Яндекс
    YANDEXLOGO = [By.XPATH, './/img[@alt="Yandex"]']
    #локатор текста Дзен
    DZEN = [By.XPATH, './/span[@aria-label="Логотип Дзен"]']
    #локатор картинки Скутера
    PICTURE = [By.XPATH, './/img[@alt="Scooter blueprint"]']

    #метод нажатия на всплывающее окно про куки
    def cookies_accept(self):
        button = self.find_element(MainHomePage.ACCEPTCOOKIE, time=10)
        button.click()


    #метод нажатия на верхнюю кнопку "Заказать"
    def upper_order_click(self):
        upper_button = self.find_element(MainHomePage.UPPERORDER,time=5)
        upper_button.click()

    # метод нажатия на нижнюю кнопку "Заказать"
    def lower_order_click(self):
        lower_button = self.find_element(MainHomePage.LOWERORDER, time=5)
        lower_button.click()

    #метод на нахождение текста
    def get_line_text(self, locator):
        WebDriverWait(self, 3)
        message = self.find_element(locator, time=10)
        return message

    #метод нажатия на первую строку
    def one_line_click(self):
        self.find_element(MainHomePage.ONELINE,time=10).click()

    #метод нажатия на вторую строку
    def two_line_click(self):
        self.find_element(MainHomePage.TWOLINE,time=10).click()

    # метод нажатия на третью строку
    def three_line_click(self):
        self.find_element(MainHomePage.THREELINE,time=10).click()

    # метод нажатия на четвертую строку
    def four_line_click(self):
        self.find_element(MainHomePage.FOURLINE,time=10).click()

    # метод нажатия на пятую строку
    def five_line_click(self):
        self.find_element(MainHomePage.FIVELINE,time=10).click()

    # метод нажатия на шестую строку
    def six_line_click(self):
        self.find_element(MainHomePage.SIXLINE,time=10).click()

    # метод нажатия на седьмую строку
    def seven_line_click(self):
        self.find_element(MainHomePage.SEVENLINE,time=10).click()

    # метод нажатия на восьмую строку
    def eight_line_click(self):
        self.find_element(MainHomePage.EIGHTLINE,time=10).click()

    #метод прокрутки страницы до раздела "Вопросы о важном"
    def scroll_to_down(self):
        self.scroll_to_element(MainHomePage.IMPORTANT)

    # метод нажатия на логотип Яндекс и проверка открывшейся вкладки
    def yandex_logo_click(self):
        logo = self.find_element(MainHomePage.YANDEXLOGO,time=10)
        logo.click()

    #метод нахождения текста Дзен
    def dzen_text_find(self):
        dzen = self.find_element(MainHomePage.DZEN,time=10)
        return dzen
