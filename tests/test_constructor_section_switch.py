from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators as lc


def test_constructor_section_switch():
    # Инициализация веб-драйвера
    driver = webdriver.Chrome()

    try:
        # Открытие главной страницы
        driver.get(lc.MAIN_PAGE_URL)

        # Ожидание загрузки страницы и видимости вкладки "Соусы"
        wait = WebDriverWait(driver, 10)

        # Переход в раздел "Соусы" и проверка класса
        sauces_tab = wait.until(EC.element_to_be_clickable((By.XPATH, lc.SAUCES_TAB)))
        sauces_tab.click()

        # Проверка изменения класса на активный
        sauces_tab_parent = wait.until(
            EC.presence_of_element_located((By.XPATH,
                                            f'//div[contains(@class, "tab_tab__1SPyG") and contains(@class, "{lc.ACTIVE_TAB_CLASS}")]/span[text()="Соусы"]'))
        )
        assert sauces_tab_parent, "Соусы: Переход не произошел"

        # Переход в раздел "Начинки" и проверка класса
        fillings_tab = wait.until(EC.element_to_be_clickable((By.XPATH, lc.FILLINGS_TAB)))
        fillings_tab.click()

        fillings_tab_parent = wait.until(
            EC.presence_of_element_located((By.XPATH,
                                            f'//div[contains(@class, "tab_tab__1SPyG") and contains(@class, "{lc.ACTIVE_TAB_CLASS}")]/span[text()="Начинки"]'))
        )
        assert fillings_tab_parent, "Начинки: Переход не произошел"

        # Переход в раздел "Булки" и проверка класса
        buns_tab = wait.until(EC.element_to_be_clickable((By.XPATH, lc.BUNS_TAB)))
        buns_tab.click()

        buns_tab_parent = wait.until(
            EC.presence_of_element_located((By.XPATH,
                                            f'//div[contains(@class, "tab_tab__1SPyG") and contains(@class, "{lc.ACTIVE_TAB_CLASS}")]/span[text()="Булки"]'))
        )
        assert buns_tab_parent, "Булки: Переход не произошел"

        print("Все переходы успешно проверены.")

    finally:
        # Закрытие браузера
        driver.quit()
