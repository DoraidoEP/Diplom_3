from selenium.webdriver.common.by import By


class LoginPageLocators:
    # Поле ввода Email
    INPUT_EMAIL = [By.XPATH, './/label[text() = "Email"]/following-sibling::input']
    # Поле ввода Пароль
    INPUT_PASSWORD = [By.XPATH, './/label[text() = "Пароль"]/following-sibling::input']
    # Кнопка "Войти" на странице входа
    LOGIN_BUTTON = [By.XPATH, './/button[text() = "Войти"]']
    # Кнопка "Восстановить пароль"
    RECOVER_PASSWORD_BUTTON = [By.XPATH, './/a[text() = "Восстановить пароль"]']