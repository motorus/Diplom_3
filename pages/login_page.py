import allure
from pages.base_page import BasePage
from urls import URLS
from locators.login_page_locators import LoginLocators
from locators.password_locators import ForgotPasswordLocators


class LoginPage(BasePage):
    @allure.step("Клик по кнопке восстановления пароля")
    def click_to_recover_password(self):
        self.open_page(URLS.LOGIN)
        self.click_to_element(LoginLocators.RECOVER_PASSWORD)
        return self.wait_and_find_element(ForgotPasswordLocators.FORGOT_PASSWORD_TEXT).text


