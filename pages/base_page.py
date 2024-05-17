import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ждем и ищем элемент по локатору")
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 5).until((expected_conditions.visibility_of_element_located(locator)))
        return self.driver.find_element(*locator)

    @allure.step("Вбиваем текст в элемент найденный по локатору")
    def send_keys_to_locator(self, locator, text):
        self.wait_and_find_element(locator).send_keys(text)

    @allure.step("Получаем текст элемента найденного по локатору")
    def get_text_locator(self, locator):
        return self.wait_and_find_element(locator).text

    @allure.step("Ждем пока элемент не станет кликабельным и кликаем по нему")
    def click_to_element(self, locator):

        WebDriverWait(self.driver, 5).until((expected_conditions.element_to_be_clickable(locator)))
        element = self.driver.find_element(*locator)

        #  self.driver.execute_script("arguments[0].click();", element)  # этот костыль здесь почему то не работает

        # костыль который позволляет проходить тестам на ФФ. Связано с тем что какое то время поверх найденного
        # элемента располагается еще 1 элемент. Невидимый. Но вызывает ошибку:
        # selenium.common.exceptions.ElementClickInterceptedException: Message: Element < button
        # class ="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa" >
        # is not clickable at point (957, 549) because another element
        # < div class ="Modal_modal_overlay__x2ZCr" > obscures it
        attempt_count = 1000000
        for i in range(attempt_count):
            try:
                element.click()
                break
            except ElementClickInterceptedException:
                pass

    @allure.step("Открываем страницу по URL")
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Проверяем что элемент отображается на странице")
    def check_element_is_displayed(self, locator):
        return self.wait_and_find_element(locator).is_displayed()

    @staticmethod
    @allure.step("Генерируем локатор из динамических данных")
    def format_locator(locator, param):
        search_type, search_text = locator
        return (search_type, search_text.format(param))

    @allure.step("Возвращаем url текущей страницы")
    def return_page_url(self):
        return self.driver.current_url

    @allure.step("Перетягиваем элемент из локатора в локатор")
    def drag_and_drop_element(self, locator_from, locator_to):
        element_from = self.wait_and_find_element(locator_from)
        element_to = self.wait_and_find_element(locator_to)
        actions_chain = ActionChains(self.driver)
        actions_chain.drag_and_drop(element_from, element_to).pause(2).perform()
