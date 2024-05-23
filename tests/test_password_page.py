import allure
from pages.password_pages import PasswordPage
from urls import URLS


class TestPasswordPage:
    @allure.title("Проверка ввода email")
    def test_insert_email(self, driver, new_user):
        password_page = PasswordPage(driver)
        email = new_user[1]["email"]
        assert password_page.insert_email_address(email) == URLS.RESET_PASS

    @allure.title("Проверка подсветки поля пароль при нажатии кнопки 'Показать/скрыть пароль'")
    def test_show_password(self, driver, new_user):
        password_page = PasswordPage(driver)
        email = new_user[1]["email"]
        password_page.insert_email_address(email)

        elements_class = password_page.check_password_field()
        assert "input__placeholder-focused" in elements_class





