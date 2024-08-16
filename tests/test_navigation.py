from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators as lc


def login(driver):
    "Функция для авторизации на сайте"
    driver.get(lc.MAIN_PAGE_URL)

    # Ожидание загрузки кнопки "Войти в аккаунт" и клик по ней
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, lc.LOGIN_BUTTON_MAIN_PAGE))
    ).click()

    # Ожидание загрузки поля email и ввод данных
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, lc.EMAIL_FIELD))
    ).send_keys(lc.TEST_EMAIL)

    # Ожидание загрузки поля пароля и ввод данных
    driver.find_element(By.XPATH, lc.PASSWORD_FIELD).send_keys(lc.TEST_PASSWORD)

    # Ожидание загрузки кнопки "Войти" и клик по ней
    driver.find_element(By.XPATH, lc.LOGIN_SUBMIT_BUTTON).click()


def navigate_to_profile(driver):
    "Функция для перехода на страницу Личного кабинета"
    # Ожидание загрузки страницы после авторизации и клик по "Личный кабинет"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, lc.PROFILE_BUTTON))
    ).click()


def test_navigation_to_constructor():
    "Тест на проверку перехода по клику на кнопку «Конструктор»"
    driver = webdriver.Chrome()
    try:
        login(driver)
        navigate_to_profile(driver)

        # Ожидание загрузки кнопки "Конструктор" и клик по ней
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, lc.CONSTRUCTOR_BUTTON))
        ).click()

        # Ожидание загрузки заголовка конструктора
        header_text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, lc.CONSTRUCTOR_HEADER))
        ).text

        assert header_text == "Соберите бургер"
    finally:
        driver.quit()


def test_navigation_to_main_page_by_logo():
    "Тест на проверку перехода по клику на логотип Stellar Burgers"
    driver = webdriver.Chrome()
    try:
        login(driver)
        navigate_to_profile(driver)

        # Ожидание загрузки логотипа и клик по нему
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, lc.LOGO))
        ).click()

        # Ожидание загрузки заголовка конструктора
        header_text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, lc.CONSTRUCTOR_HEADER))
        ).text

        assert header_text == "Соберите бургер"
    finally:
        driver.quit()


# Запуск тестов
if __name__ == "__main__":
    test_navigation_to_constructor()
    test_navigation_to_main_page_by_logo()
