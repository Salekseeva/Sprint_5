from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators as lc


def login(browser):
    "Функция для авторизации на сайте"
    browser.get(lc.MAIN_PAGE_URL)

    # Ожидание загрузки кнопки "Войти в аккаунт" и клик по ней
    login_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, lc.LOGIN_BUTTON_MAIN_PAGE))
    )
    login_button.click()

    # Ожидание загрузки поля email и ввод данных
    email_field = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, lc.EMAIL_FIELD))
    )
    email_field.send_keys(lc.TEST_EMAIL)

    # Ожидание загрузки поля пароля и ввод данных
    password_field = browser.find_element(By.XPATH, lc.PASSWORD_FIELD)
    password_field.send_keys(lc.TEST_PASSWORD)

    # Клик по кнопке "Войти"
    submit_button = browser.find_element(By.XPATH, lc.LOGIN_SUBMIT_BUTTON)
    submit_button.click()


def navigate_to_profile(browser):
    "Функция для перехода на страницу Личного кабинета"
    # Ожидание и клик по "Личный кабинет"
    profile_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, lc.PROFILE_BUTTON))
    )
    profile_button.click()


def test_navigation_to_constructor(browser):
    "Тест на проверку перехода по клику на кнопку «Конструктор»"
    login(browser)
    navigate_to_profile(browser)

    # Ожидание и клик по кнопке "Конструктор"
    constructor_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, lc.CONSTRUCTOR_BUTTON))
    )
    constructor_button.click()

    # Ожидание и проверка заголовка конструктора
    header_text = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, lc.CONSTRUCTOR_HEADER))
    ).text

    assert header_text == "Соберите бургер"

def test_navigation_to_main_page_by_logo(browser):
    "Тест на проверку перехода по клику на логотип Stellar Burgers"
    login(browser)
    navigate_to_profile(browser)

    # Ожидание и клик по логотипe
    logo_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, lc.LOGO))
    )
    logo_button.click()

    # Ожидание и проверка заголовка конструктора
    header_text = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, lc.CONSTRUCTOR_HEADER))
    ).text

    assert header_text == "Соберите бургер"

