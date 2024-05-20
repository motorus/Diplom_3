import allure
from pages.base_page import BasePage
from urls import URLS
from locators.login_page_locators import LoginLocators


class LoginPage(BasePage):
    @allure.step("Клик по кнопке восстановления пароля")
    def click_to_recover_password(self):
        self.open_page(URLS.LOGIN)
        self.click_to_element(LoginLocators.RECOVER_PASSWORD)
        return self.return_page_url()
