from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators as lc  # Импортируем все локаторы и данные из файла locators.py

def generate_random_email():
    # Функция для генерации случайного email
    import random
    import string
    return ''.join(random.choices(string.ascii_lowercase, k=8)) + "@ya.ru"

# Тест проверяет, что при правильном заполнении всех полей пользователь успешно переходит на страницу входа.
def test_registration_success():
    driver = webdriver.Chrome()
    driver.get(lc.MAIN_PAGE_URL)  # Используем URL главной страницы из файла locators.py

    try:
        # Нажатие на ссылку "Личный кабинет"
        personal_account_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, lc.PROFILE_BUTTON))  # Локатор из locators.py
        )
        personal_account_link.click()

        # Нажатие на ссылку для перехода к регистрации
        register_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, lc.REGISTRATION_LOGIN_LINK))  # Локатор из locators.py
        )
        register_link.click()

        # Заполнение поля "Имя"
        name_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, lc.NAME_FIELD))
        )
        name_field.send_keys("TestUser")

        # Заполнение поля "Email"
        email_field = driver.find_element(By.XPATH, lc.EMAIL_FIELD_REG)
        email_field.send_keys(generate_random_email())

        # Заполнение поля "Пароль"
        password_field = driver.find_element(By.XPATH, lc.PASSWORD_FIELD_REG)
        password_field.send_keys("password123")

        # Нажатие кнопки "Зарегистрироваться"
        register_button = driver.find_element(By.XPATH, lc.REGISTER_BUTTON)
        register_button.click()

        # Ожидание перехода на страницу входа
        WebDriverWait(driver, 10).until(
            EC.url_to_be(lc.LOGIN_URL)  # Используем URL страницы логина из файла locators.py
        )

        print("Тест на успешную регистрацию пройден.")

    finally:
        driver.quit()

# Тест проверяет, что при вводе некорректного пароля появляется сообщение об ошибке и
# поле пароля получает правильный CSS-класс ошибки.
def test_registration_invalid_password():
    driver = webdriver.Chrome()
    driver.get(lc.MAIN_PAGE_URL)

    try:
        # Нажатие на ссылку "Личный кабинет"
        personal_account_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, lc.PROFILE_BUTTON))
        )
        personal_account_link.click()

        # Нажатие на ссылку для перехода к регистрации
        register_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, lc.REGISTRATION_LOGIN_LINK))
        )
        register_link.click()

        # Заполнение поля "Имя"
        name_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, lc.NAME_FIELD))
        )
        name_field.send_keys("TestUser")

        # Заполнение поля "Email"
        email_field = driver.find_element(By.XPATH, lc.EMAIL_FIELD_REG)
        email_field.send_keys(generate_random_email())

        # Заполнение поля "Пароль" некорректным значением (менее 6 символов)
        password_field = driver.find_element(By.XPATH, lc.PASSWORD_FIELD_REG)
        password_field.send_keys("123")

        # Нажатие кнопки "Зарегистрироваться"
        register_button = driver.find_element(By.XPATH, lc.REGISTER_BUTTON)
        register_button.click()

        # Ожидание появления сообщения об ошибке
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, lc.ERROR_MESSAGE))
        )

        # Проверка сообщения об ошибке
        assert "Некорректный пароль" in error_message.text, "Ошибка в сообщении об ошибке."

        # Проверка активации класса .input_status_error
        password_field_parent = driver.find_element(By.XPATH, lc.PASSWORD_FIELD_PARENT)
        password_field_class = password_field_parent.get_attribute("class")
        assert "input_status_error" in password_field_class, "Класс поля пароля не изменился на ошибочный."

        print("Тест на некорректный пароль пройден.")

    finally:
        driver.quit()

# Запуск тестов
if __name__ == "__main__":
    test_registration_success()
    test_registration_invalid_password()
