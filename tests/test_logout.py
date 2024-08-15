import pytest
from selenium import webdriver  # Добавлен импорт webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators as lc


@pytest.fixture
def driver():
    # Инициализация WebDriver
    driver = webdriver.Chrome()  # Убедитесь, что путь к ChromeDriver указан корректно
    driver.maximize_window()
    yield driver
    driver.quit()


def login(driver):
    "Функция авторизации на сайте. Выполняет действия по вводу email, пароля и нажатию кнопки входа. Затем переходит в личный кабинет."
    # Открыть главную страницу сайта
    driver.get(lc.MAIN_PAGE_URL)

    # Нажать на кнопку «Войти в аккаунт»
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, lc.LOGIN_BUTTON_MAIN_PAGE))
    ).click()

    # Ввести email
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, lc.EMAIL_FIELD))
    ).send_keys(lc.TEST_EMAIL)

    # Ввести пароль
    driver.find_element(By.XPATH, lc.PASSWORD_FIELD).send_keys(lc.TEST_PASSWORD)

    # Нажать кнопку Войти
    driver.find_element(By.XPATH, lc.LOGIN_SUBMIT_BUTTON).click()

    # Нажать на кнопку «Личный кабинет»
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, lc.PROFILE_BUTTON))
    ).click()


def test_logout(driver):
    "Тест на проверку выхода из аккаунта. Выполняет авторизацию и затем тестирует функцию выхода, проверяя URL страницы."
    # Выполнить авторизацию
    login(driver)

    # Нажать кнопку «Выход»
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, lc.LOGOUT_SUBMIT_BUTTON))
    ).click()

    # Проверить, что произошел переход на страницу Авторизации
    WebDriverWait(driver, 10).until(
        EC.url_to_be(lc.LOGIN_URL)
    )
    assert driver.current_url == lc.LOGIN_URL, "Не произошел выход из аккаунта!"
