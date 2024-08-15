import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators as lc


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def login(browser, email, password):
    # Ожидаем, что загрузится страница авторизации
    WebDriverWait(browser, 10).until(EC.url_to_be(lc.LOGIN_URL))
    email_field = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, lc.EMAIL_FIELD)))
    email_field.send_keys(email)
    password_field = browser.find_element(By.XPATH, lc.PASSWORD_FIELD)
    password_field.send_keys(password)
    login_button = browser.find_element(By.XPATH, lc.LOGIN_SUBMIT_BUTTON)
    login_button.click()

    # Ожидаем переход на главную страницу
    WebDriverWait(browser, 10).until(EC.url_to_be(lc.MAIN_PAGE_URL))
    # Проверяем, что текст кнопки изменился на "Оформить заказ"
    order_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, lc.ORDER_BUTTON_MAIN_PAGE)))
    assert order_button.text == "Оформить заказ", "Авторизация не выполнена"


def test_login_button_main_page(browser):
    browser.get(lc.MAIN_PAGE_URL)
    login_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, lc.LOGIN_BUTTON_MAIN_PAGE)))
    login_button.click()
    login(browser, lc.TEST_EMAIL, lc.TEST_PASSWORD)


def test_login_via_profile_button(browser):
    browser.get(lc.MAIN_PAGE_URL)
    profile_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, lc.PROFILE_BUTTON)))
    profile_button.click()
    login(browser, lc.TEST_EMAIL, lc.TEST_PASSWORD)


def test_login_via_registration_form(browser):
    browser.get(lc.MAIN_PAGE_URL)
    profile_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, lc.PROFILE_BUTTON)))
    profile_button.click()

    # Переход к форме регистрации
    registration_login_link = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, lc.REGISTRATION_LOGIN_LINK)))
    registration_login_link.click()

    # Переход к странице авторизации
    login_link_reg = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, lc.LOGIN_LINK_REG)))
    login_link_reg.click()

    # Проверяем, что открылась страница авторизации
#    WebDriverWait(browser, 10).until(EC.url_to_be(lc.LOGIN_URL))
    login(browser, lc.TEST_EMAIL, lc.TEST_PASSWORD)


def test_login_via_forgot_password(browser):
    browser.get(lc.MAIN_PAGE_URL)
    login_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, lc.LOGIN_BUTTON_MAIN_PAGE)))
    login_button.click()

    # Переход к форме восстановления пароля
    forgot_password_link = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, lc.FORGOT_PASSWORD_LINK)))
    forgot_password_link.click()

    # Проверка, что открылась нужная страница восстановления пароля
    WebDriverWait(browser, 10).until(EC.url_to_be(lc.FORGOT_PASSWORD_URL))

    # Переход к авторизации с формы восстановления пароля
    login_button_forgot_password = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, lc.LOGIN_BUTTON_FORGOT_PASSWORD)))
    login_button_forgot_password.click()

    # Ожидаем переход на главную страницу после авторизации
    login(browser, lc.TEST_EMAIL, lc.TEST_PASSWORD)
