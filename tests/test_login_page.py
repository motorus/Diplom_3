import allure
from pages.login_page import LoginPage


class TestLoginPage:
    @allure.title("Проверка нажатия на кнопку 'Восстановить пароль'")
    def test_click_to_recover_password_success(self, driver):

        login_page = LoginPage(driver)
        assert "Восстановление пароля" in login_page.click_to_recover_password()


