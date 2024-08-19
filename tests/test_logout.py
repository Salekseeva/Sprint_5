from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators as lc


def login(browser):
    "Функция авторизации на сайте. Выполняет действия по вводу email, пароля и нажатию кнопки входа. Затем переходит в личный кабинет."
    # Открыть главную страницу сайта
    browser.get(lc.MAIN_PAGE_URL)

    # Нажать на кнопку «Войти в аккаунт» и найти поле для ввода email
    login_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, lc.LOGIN_BUTTON_MAIN_PAGE))
    )
    login_button.click()

    # Ввести email и пароль
    email_field = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, lc.EMAIL_FIELD))
    )
    email_field.send_keys(lc.TEST_EMAIL)
    browser.find_element(By.XPATH, lc.PASSWORD_FIELD).send_keys(lc.TEST_PASSWORD)

    # Нажать кнопку Войти и перейти в личный кабинет
    browser.find_element(By.XPATH, lc.LOGIN_SUBMIT_BUTTON).click()
    profile_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, lc.PROFILE_BUTTON))
    )
    profile_button.click()


def test_logout(browser):
    "Тест на проверку выхода из аккаунта. Выполняет авторизацию и затем тестирует функцию выхода, проверяя URL страницы."
    # Выполнить авторизацию
    login(browser)

    # Нажать кнопку «Выход» и проверить переход на страницу Авторизации
    logout_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, lc.LOGOUT_SUBMIT_BUTTON))
    )
    logout_button.click()
    WebDriverWait(browser, 10).until(
        EC.url_to_be(lc.LOGIN_URL)
    )
    # Проверить текущий URL
    assert browser.current_url == lc.LOGIN_URL, "Не произошел выход из аккаунта!"
