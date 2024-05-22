
from pages.account_page import AccountPage
from urls import URLS
import allure


class TestAccount:
    @allure.title("Проверка нажатия на кнопку 'История заказов'")
    def test_click_to_order_history(self, driver, logged_driver):
        account_page = AccountPage(driver)
        assert account_page.click_to_order_history() == URLS.ORDER_HISTORY

    @allure.title("Проверка нажатия на кнопку 'Выход'")
    def test_click_to_exit(self, driver, logged_driver):
        account_page = AccountPage(driver)
        assert account_page.click_to_exit_button() == URLS.LOGIN

    @allure.title("Проверка нажатия на кнопку 'Конструктор'")
    def test_click_to_constructor(self, driver, logged_driver):
        account_page = AccountPage(driver)
        assert account_page.click_to_constructor_button() == URLS.MAIN
