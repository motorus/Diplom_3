import allure
from pages.order_feed_page import OrderFeed


class TestOrderFeed:
    @allure.title("Проверка открытия информации о заказе из ленты заказов")
    def test_open_order_info(self, driver):
        order_feed = OrderFeed(driver)
        assert order_feed.open_order_info()

    @allure.title("Проверка отображения личных заказов в общей ленте заказов")
    def test_check_private_orders_in_feed(self, driver, logged_driver, new_user):
        order_feed = OrderFeed(driver)
        assert order_feed.check_private_orders_in_feed(new_user)

    @allure.title("Проверка увеличения счетчика заказов за сегодня и за все время при создании заказа")
    def test_check_order_counter(self, driver, logged_driver, new_user):
        order_feed = OrderFeed(driver)
        assert order_feed.check_order_counter(new_user)

    @allure.title("Проверка отображения созданного заказа в поле 'В работе'")
    def test_check_order_in_progress(self, driver, logged_driver, new_user):
        order_feed = OrderFeed(driver)
        assert order_feed.check_order_in_progress(new_user)
