from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators as lc


def test_login_and_navigate_to_profile(browser):
    # Открыть главную страницу сайта
    browser.get(lc.MAIN_PAGE_URL)

    # Ожидание загрузки и нажатие на кнопку «Личный кабинет»
    profile_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, lc.PROFILE_BUTTON))
    )
    profile_button.click()

    # Ожидание загрузки страницы авторизации и ввод email и пароля
    email_field = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, lc.EMAIL_FIELD))
    )
    email_field.send_keys(lc.TEST_EMAIL)

    password_field = browser.find_element(By.XPATH, lc.PASSWORD_FIELD)
    password_field.send_keys(lc.TEST_PASSWORD)

    # Нажатие на кнопку «Войти»
    login_button = browser.find_element(By.XPATH, lc.LOGIN_SUBMIT_BUTTON)
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
