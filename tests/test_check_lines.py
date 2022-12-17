from pages.home_page import MainHomePage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


#проверка первой строки на главной странице
def test_check_text_first_line_is_correct(browser):
    main = MainHomePage(browser)
    main.go_to_site()
    main.cookies_accept()
    WebDriverWait(browser, 3)
    important = main.find_element(MainHomePage.IMPORTANT)
    browser.execute_script("return arguments[0].scrollIntoView();", important)
    WebDriverWait(browser, 3).until(
        expected_conditions.element_to_be_clickable(MainHomePage.ONELINE))
    main.one_line_click()
    WebDriverWait(browser, 5).until(
        expected_conditions.presence_of_element_located(MainHomePage.ONELINETEXT))
    message_text = main.get_line_text(MainHomePage.ONELINETEXT)
    assert message_text.text == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."


#проверка второй строки на главной странице
def test_check_text_second_line_is_correct(browser):
    main = MainHomePage(browser)
    main.go_to_site()
    main.cookies_accept()
    WebDriverWait(browser, 3)
    important = main.find_element(MainHomePage.IMPORTANT)
    browser.execute_script("return arguments[0].scrollIntoView();", important)
    WebDriverWait(browser, 3).until(
        expected_conditions.element_to_be_clickable(MainHomePage.TWOLINE))
    main.two_line_click()
    WebDriverWait(browser, 5).until(
        expected_conditions.visibility_of_element_located(MainHomePage.TWOLINETEXT))
    message_text = main.get_line_text(MainHomePage.TWOLINETEXT)
    assert message_text.text == "Пока что у нас так: один заказ — один самокат. " \
                                  "Если хотите покататься с друзьями, " \
                                  "можете просто сделать несколько заказов — один за другим."


 #проверка третьей строки на главной странице
def test_check_text_third_line_is_correct(browser):
    main = MainHomePage(browser)
    main.go_to_site()
    main.cookies_accept()
    WebDriverWait(browser, 3)
    important = main.find_element(MainHomePage.IMPORTANT)
    browser.execute_script("return arguments[0].scrollIntoView();", important)
    WebDriverWait(browser, 3).until(
        expected_conditions.element_to_be_clickable(MainHomePage.THREELINE))
    main.three_line_click()
    WebDriverWait(browser, 5).until(
        expected_conditions.visibility_of_element_located(MainHomePage.THREELINETEXT))
    message_text = main.get_line_text(MainHomePage.THREELINETEXT)
    assert message_text.text == "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. " \
                                "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. " \
                                "Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."


#проверка четвертой строки на главной странице
def test_check_text_fourth_line_is_correct(browser):
    main = MainHomePage(browser)
    main.go_to_site()
    main.cookies_accept()
    WebDriverWait(browser, 3)
    important = main.find_element(MainHomePage.IMPORTANT)
    browser.execute_script("return arguments[0].scrollIntoView();", important)
    WebDriverWait(browser, 3).until(
        expected_conditions.element_to_be_clickable(MainHomePage.FOURLINE))
    main.four_line_click()
    WebDriverWait(browser, 5).until(
        expected_conditions.visibility_of_element_located(MainHomePage.FOURLINETEXT))
    message_text = main.get_line_text(MainHomePage.FOURLINETEXT)
    assert message_text.text == "Только начиная с завтрашнего дня. Но скоро станем расторопнее."


#проверка пятой строки на главной странице
def test_check_text_fifth_line_is_correct(browser):
    main = MainHomePage(browser)
    main.go_to_site()
    main.cookies_accept()
    WebDriverWait(browser, 3)
    important = main.find_element(MainHomePage.IMPORTANT)
    browser.execute_script("return arguments[0].scrollIntoView();", important)
    WebDriverWait(browser, 3).until(
        expected_conditions.element_to_be_clickable(MainHomePage.FIVELINE))
    main.five_line_click()
    WebDriverWait(browser, 5).until(
        expected_conditions.visibility_of_element_located(MainHomePage.FIVELINETEXT))
    message_text = main.get_line_text(MainHomePage.FIVELINETEXT)
    assert message_text.text == "Пока что нет! Но если что-то срочное" \
                                " — всегда можно позвонить в поддержку по красивому номеру 1010."


#проверка шестой строки на главной странице
def test_check_text_sixth_line_is_correct(browser):
    main = MainHomePage(browser)
    main.go_to_site()
    main.cookies_accept()
    WebDriverWait(browser, 3)
    important = main.find_element(MainHomePage.IMPORTANT)
    browser.execute_script("return arguments[0].scrollIntoView();", important)
    WebDriverWait(browser, 3).until(
        expected_conditions.element_to_be_clickable(MainHomePage.SIXLINE))
    main.six_line_click()
    WebDriverWait(browser, 5).until(
        expected_conditions.visibility_of_element_located(MainHomePage.SIXLINETEXT))
    message_text = main.get_line_text(MainHomePage.SIXLINETEXT)
    assert message_text.text == "Самокат приезжает к вам с полной зарядкой. " \
                                "Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. " \
                                "Зарядка не понадобится."


#проверка седьмой строки на главной странице
def test_check_text_seventh_line_is_correct(browser):
    main = MainHomePage(browser)
    main.go_to_site()
    main.cookies_accept()
    WebDriverWait(browser, 3)
    important = main.find_element(MainHomePage.IMPORTANT)
    browser.execute_script("return arguments[0].scrollIntoView();", important)
    WebDriverWait(browser, 3).until(
        expected_conditions.element_to_be_clickable(MainHomePage.SEVENLINE))
    main.seven_line_click()
    WebDriverWait(browser, 5).until(
        expected_conditions.visibility_of_element_located(MainHomePage.SEVENLINETEXT))
    message_text = main.get_line_text(MainHomePage.SEVENLINETEXT)
    assert message_text.text == "Да, пока самокат не привезли. " \
                                "Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."


#проверка восьмой строки на главной странице
def test_check_text_eighth_line_is_correct(browser):
    main = MainHomePage(browser)
    main.go_to_site()
    main.cookies_accept()
    WebDriverWait(browser, 3)
    important = main.find_element(MainHomePage.IMPORTANT)
    browser.execute_script("return arguments[0].scrollIntoView();", important)
    WebDriverWait(browser, 3).until(
        expected_conditions.element_to_be_clickable(MainHomePage.EIGHTLINE))
    main.eight_line_click()
    WebDriverWait(browser, 5).until(
        expected_conditions.visibility_of_element_located(MainHomePage.EIGHTLINETEXT))
    message_text = main.get_line_text(MainHomePage.EIGHTLINETEXT)
    assert message_text.text == "Да, обязательно. Всем самокатов! И Москве, и Московской области."
