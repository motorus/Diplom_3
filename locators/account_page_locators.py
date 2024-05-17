from selenium.webdriver.common.by import By


class AccountLocators:
    """Локаторы личного кабинета"""
    ORDER_HISTORY = By.XPATH, "//a[@href='/account/order-history']"  # Кнопка 'История заказов'
    EXIT_BUTTON = By.XPATH, "//button[contains(text(), 'Выход')]"  # Кнопка выхода
    CONSTRUCTOR_BUTTON = By.XPATH, "//p[contains(text(), 'Конструктор')]"  # Кнопка конструктора
    PERSONAL_AREA_TEXT = By.XPATH, ("//p[contains(text(),"
                                    "'В этом разделе вы можете изменить "
                                    "свои персональные данные')]")  # Тест из личного кабинета
