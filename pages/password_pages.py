import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from urls import URLS
from locators.password_locators import ForgotPasswordLocators, ResetPasswordLocators


class PasswordPage(BasePage):
    @allure.step("Восстановление пароля. Ввод email")
    def insert_email_address(self, email):
        self.open_page(URLS.FORGOT_PASS)

        self.click_to_element(ForgotPasswordLocators.FORGOT_PASSWORD_LABEL)
        self.send_keys_to_locator(ForgotPasswordLocators.FORGOT_PASSWORD_FIELD, email)
        self.click_to_element(ForgotPasswordLocators.RECOVER_BUTTON)

        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(ResetPasswordLocators.CODE_FILED))

        return self.return_page_url()

    @allure.step("Получение имени класса элемента 'Поле ввода пароль'")
    def check_password_field(self):
        self.click_to_element(ResetPasswordLocators.SHOW_PASSWORD)
        return self.wait_and_find_element(ResetPasswordLocators.PASSWORD_FOCUSED).get_attribute("class")




