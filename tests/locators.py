# URL-адреса
MAIN_PAGE_URL = "https://stellarburgers.nomoreparties.site/"  # URL главной страницы
LOGIN_URL = MAIN_PAGE_URL + "login"  # URL страницы авторизации
FORGOT_PASSWORD_URL = MAIN_PAGE_URL + "forgot-password"  # URL страницы восстановления пароля
PROFILE_PAGE_URL = MAIN_PAGE_URL + "account/profile"  # URL личного кабинета после авторизации
REGISTRATION_PAGE_URL = "https://stellarburgers.nomoreparties.site/register"  # URL страницы регистрации
LOGIN_PAGE_URL = "https://stellarburgers.nomoreparties.site/login"  # URL страницы логина

# Тестовые данные
TEST_EMAIL = "testtestov1999@yandex.ru"
TEST_PASSWORD = "123456"

# Локаторы
LOGIN_BUTTON_MAIN_PAGE = '//button[text()="Войти в аккаунт"]'  # Кнопка «Войти в аккаунт» на главной странице
REGISTRATION_LOGIN_LINK = '//div/p[1]/a'  # Кнопка/ссылка в форме регистрации "Зарегистрироваться"
LOGIN_BUTTON_FORGOT_PASSWORD = '//a[text()="Войти"]'  # Кнопка "Войти" на странице восстановления пароля
PROFILE_BUTTON = '//div/header/nav/a'  # Кнопка «Личный кабинет»
CONSTRUCTOR_BUTTON = '//p[text()="Конструктор"]'  # Кнопка «Конструктор»
LOGO = '//*[@id="root"]/div/header/nav/div/a'  # Кликабельный логотип “Stellar Burgers”
ORDER_BUTTON_MAIN_PAGE = '//button[text()="Оформить заказ"]'  # Кнопка «Оформить заказ» на главной странице (после авторизации)

# Локаторы разделов конструктора
SAUCES_TAB = '//span[text()="Соусы"]'  # Вкладка "Соусы"
FILLINGS_TAB = '//span[text()="Начинки"]'  # Вкладка "Начинки"
BUNS_TAB = '//span[text()="Булки"]'  # Вкладка "Булки"

# Общий класс для вкладки в активном состоянии
ACTIVE_TAB_CLASS = 'tab_tab_type_current__2BEPc'  # Класс для активного состояния вкладки

# Локаторы страницы авторизации
EMAIL_FIELD = '//fieldset[1]/div/div/input'  # Поле email
PASSWORD_FIELD = '//fieldset[2]/div/div/input'  # Поле пароль
LOGIN_SUBMIT_BUTTON = '//button[text()="Войти"]'  # Кнопка «Войти»
FORGOT_PASSWORD_LINK = '//p[2]/a'  # Кнопка/ссылка "Восстановить пароль"

# Локаторы конструктора
CONSTRUCTOR_HEADER = '//h1[text()="Соберите бургер"]'  # Заголовок страницы конструктора “Собери бургер”

# Локаторы страницы "Личный кабинет"
LOGOUT_SUBMIT_BUTTON = "//button[text()='Выход']"  # Кнопка/ссылка «Выход» в "Личном кабинете"

# Локаторы страницы регистрации
# PERSONAL_ACCOUNT_LINK = '//*[@id="root"]/div/header/nav/a'  # Ссылка "Личный кабинет"
REGISTER_LINK = '//*[@id="root"]/div/main/div/div/p[1]/a'  # Ссылка для перехода к регистрации
NAME_FIELD = '//fieldset[1]/div/div/input'  # Поле ввода имени
EMAIL_FIELD_REG = '//fieldset[2]/div/div/input'  # Поле email на странице решистрации
PASSWORD_FIELD_REG = '//fieldset[3]/div/div/input'  # Поле пароль на странице регистрации
REGISTER_BUTTON = '//button[text()="Зарегистрироваться"]'  # Кнопка "Зарегистрироваться"
ERROR_MESSAGE = '//fieldset[3]/div/p'  # Сообщение об ошибке
PASSWORD_FIELD_PARENT = '//fieldset[3]/div/div'  # Родительский элемент поля пароля
LOGIN_LINK_REG = '//div/p/a[text()="Войти"]'  # Кнопка/ссылка "Войти" в форме регистрации