from locators.account_page_locators import AccountLocators
from locators.login_page_locators import LoginLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure


class AccountPage(BasePage):

    @allure.step("Клик по истории заказов в личном кабинете")
    def click_to_order_history(self):
        self.click_to_element(MainPageLocators.PERSONAL_AREA_BUTTON)
        self.click_to_element(AccountLocators.ORDER_HISTORY)
        return self.return_page_url()

    @allure.step("Клик по кнопке выход в личном кабинете")
    def click_to_exit_button(self):
        self.click_to_element(MainPageLocators.PERSONAL_AREA_BUTTON)
        self.click_to_element(AccountLocators.EXIT_BUTTON)
        return self.wait_and_find_element(LoginLocators.RECOVER_PASSWORD)

    @allure.step("Клик по кнопке конструктор")
    def click_to_constructor_button(self):
        self.click_to_element(MainPageLocators.PERSONAL_AREA_BUTTON)
        self.click_to_element(AccountLocators.CONSTRUCTOR_BUTTON)
        return self.return_page_url()
