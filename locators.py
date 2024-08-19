# URL-адреса
MAIN_PAGE_URL = "https://stellarburgers.nomoreparties.site/"  # URL главной страницы
LOGIN_URL = MAIN_PAGE_URL + "login"  # URL страницы авторизации
FORGOT_PASSWORD_URL = MAIN_PAGE_URL + "forgot-password"  # URL страницы восстановления пароля
PROFILE_PAGE_URL = MAIN_PAGE_URL + "account/profile"  # URL личного кабинета после авторизации
REGISTRATION_PAGE_URL = "https://stellarburgers.nomoreparties.site/register"  # URL страницы регистрации
LOGIN_PAGE_URL = "https://stellarburgers.nomoreparties.site/login"  # URL страницы логина

# Тестовые данные
TEST_NAME = "TestUser"
TEST_EMAIL = "testtestov1999@yandex.ru"
TEST_PASSWORD = "123456"

# Локаторы
LOGIN_BUTTON_MAIN_PAGE = '//button[text()="Войти в аккаунт"]'  # Кнопка «Войти в аккаунт» на главной странице
LOGIN_BUTTON_FORGOT_PASSWORD = '//a[text()="Войти"]'  # Кнопка "Войти" на странице восстановления пароля
PROFILE_BUTTON = '//p[text()="Личный Кабинет"]'  # Кнопка «Личный кабинет»
CONSTRUCTOR_BUTTON = '//p[text()="Конструктор"]'  # Кнопка «Конструктор»
LOGO = '//div[@class="AppHeader_header__logo__2D0X2"]/a[@href="/"]'  # Кликабельный логотип “Stellar Burgers”
ORDER_BUTTON_MAIN_PAGE = '//button[text()="Оформить заказ"]'  # Кнопка «Оформить заказ» на главной странице (после авторизации)

# Локаторы разделов конструктора
SAUCES_TAB = '//span[text()="Соусы"]'  # Вкладка "Соусы"
FILLINGS_TAB = '//span[text()="Начинки"]'  # Вкладка "Начинки"
BUNS_TAB = '//span[text()="Булки"]'  # Вкладка "Булки"

# Общий класс для вкладки в активном состоянии
ACTIVE_TAB_CLASS = 'tab_tab_type_current__2BEPc'  # Класс для активного состояния вкладки

# Локаторы страницы авторизации
EMAIL_FIELD = '//input[@name="name"]'  # Поле email
PASSWORD_FIELD = '//input[@name="Пароль"]'  # Поле пароль
LOGIN_SUBMIT_BUTTON = '//button[text()="Войти"]'  # Кнопка «Войти»
FORGOT_PASSWORD_LINK = '//a[text()="Восстановить пароль"]'  # Кнопка/ссылка "Восстановить пароль"
REGISTRATION_LOGIN_LINK = '//a[text()="Зарегистрироваться"]'  # Кнопка/ссылка "Зарегистрироваться" на странице Вход

# Локаторы конструктора
CONSTRUCTOR_HEADER = '//h1[text()="Соберите бургер"]'  # Заголовок страницы конструктора “Собери бургер”

# Локаторы страницы "Личный кабинет"
LOGOUT_SUBMIT_BUTTON = "//button[text()='Выход']"  # Кнопка/ссылка «Выход» в "Личном кабинете"

# Локаторы страницы регистрации
NAME_FIELD = '//label[text()="Имя"]/../input[@name="name"]'  # Поле ввода имени
EMAIL_FIELD_REG = '//label[text()="Email"]/../input[@name="name"]'  # Поле email на странице решистрации
PASSWORD_FIELD_REG = '//input[@name="Пароль"]'  # Поле пароль на странице регистрации
REGISTER_BUTTON = '//button[text()="Зарегистрироваться"]'  # Кнопка "Зарегистрироваться"
ERROR_MESSAGE = '//p[text()="Некорректный пароль"]'  # Сообщение об ошибке
PASSWORD_FIELD_PARENT = '//div[contains(@class, "input_type_password")]'  # Родительский элемент поля пароля
LOGIN_LINK_REG = '//a[text()="Войти"]'  # Кнопка/ссылка "Войти" в форме регистрации