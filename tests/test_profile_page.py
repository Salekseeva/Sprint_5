import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators as lc


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_login_and_navigate_to_profile(browser):
    # Открыть главную страницу сайта
    browser.get(lc.MAIN_PAGE_URL)

    # Ожидание загрузки кнопки «Личный кабинет» и нажатие на неё
    profile_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, lc.PROFILE_BUTTON))
    )
    profile_button.click()

    # Ожидание загрузки страницы авторизации и появления поля email
    email_field = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, lc.EMAIL_FIELD))
    )

    # Вводим email
    email_field.send_keys("testtestov1999@yandex.ru")

    # Ожидание поля пароля и ввод пароля
    password_field = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, lc.PASSWORD_FIELD))
    )
    password_field.send_keys("123456")

    # Ожидание кнопки «Войти» и нажатие на неё
    login_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, lc.LOGIN_SUBMIT_BUTTON))
    )
    login_button.click()

    # Ожидание успешной авторизации и появления кнопки «Личный кабинет»
    profile_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, lc.PROFILE_BUTTON))
    )
    profile_button.click()

    # Ожидание перехода на страницу профиля
    WebDriverWait(browser, 10).until(
        EC.url_to_be(lc.PROFILE_PAGE_URL)
    )

    # Проверка что URL изменился на URL личного кабинета
    assert browser.current_url == lc.PROFILE_PAGE_URL, "Переход в личный кабинет не выполнен"
