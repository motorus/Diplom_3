from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    """Локаторы восстановления пароля"""
    FORGOT_PASSWORD_TEXT = By.XPATH, "//h2[contains(text(), 'Восстановление пароля')]"  # Текст "Восстановление пароля"
    FORGOT_PASSWORD_LABEL = By.XPATH, "//label[contains(text(), 'Email')]"  # Текст "Email"
    FORGOT_PASSWORD_FIELD = By.XPATH, "//label[contains(text(), 'Email')]/parent::div/input"  # Поле ввода "Email"
    RECOVER_BUTTON = By.XPATH, "//button[contains(text(), 'Восстановить')]"  # Кнопка "Восстановить"


class ResetPasswordLocators:
    """Локаторы сброса пароля"""
    BUTTON_SAVE = By.XPATH, "//button[contains(text(), 'Сохранить')]"  # Кнопка "Сохранить"
    CODE_FILED = By.XPATH, "//label[contains(text(), 'Введите код из письма')]"  # Поле ввода для кода из письма
    NEW_PASSWORD_FIELD = By.XPATH, "//input[@name='Введите новый пароль']"  # Поле ввода нового пароля
    SHOW_PASSWORD = By.XPATH, "//input[@name='Введите новый пароль']/parent::div"  # Кнопка "Показать пароль"
    PASSWORD_FOCUSED = By.XPATH, "//input[@name='Введите новый пароль']/parent::div/label"  # Активность поля ввода пароля
