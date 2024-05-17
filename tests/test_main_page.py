import allure
import helps
import pytest

from pages.main_page import MainPage


class TestMainPage:

    @allure.title("Проверка перехода в личный кабинет")
    def test_click_personal_area(self, logged_driver):

        main_page = MainPage(logged_driver)
        assert main_page.click_to_personal_area()

    @allure.title("Проверка перехода на ленту заказов")
    def test_click_to_orders_feed(self, logged_driver):
        main_page = MainPage(logged_driver)
        assert MainPage.click_to_orders_feed(main_page) == "Выполнено за все время:"

    @allure.title("Проверка нажатия на инридиент. Открытие формы с описанием ингредиента")
    @pytest.mark.parametrize("ingredient", helps.Order.get_ingredients()[1])
    def test_click_to_ingredient(self, driver, ingredient):
        main_page = MainPage(driver)
        assert main_page.click_to_ingredient(ingredient) == "Детали ингредиента"

    @allure.title("Проверка нажатия на кнопку закрытия формы деталей игредиента")
    def test_close_ingredient_details(self, driver):
        main_page = MainPage(driver)
        assert main_page.click_to_ingredient_and_close()

    @allure.title("Проверка того что при добавлении игредиента в заказа счетчик игредиента увеличивается")
    def test_add_ingredient_check_counter(self, driver):
        main_page = MainPage(driver)
        assert main_page.check_counter_of_ingredient()

    @allure.title("Проверка что залогиненный пользователь может создать заказ")
    def test_user_create_order(self, logged_driver):
        main_page = MainPage(logged_driver)
        assert main_page.create_order()





