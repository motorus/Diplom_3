import allure
from pages.login_page import LoginPage
from urls import URLS


class TestLoginPage:
    @allure.title("Проверка нажатия на кнопку 'Восстановить пароль'")
    def test_click_to_recover_password_success(self, driver):
        login_page = LoginPage(driver)

        assert login_page.click_to_recover_password() == URLS.FORGOT_PASS


