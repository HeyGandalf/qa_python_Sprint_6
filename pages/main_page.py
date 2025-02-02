import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from helpers.locators import BasePageLocator
from helpers.locators import ScooterMainPageLocator as Locators
from pages.base_page import BasePage


class ScooterMainPage(BasePage):
    @allure.step('Нажать на кнопку "Заказать" в правом верхнем углу страницы')
    def click_top_order_button(self):
        return self.find_element(Locators.TOP_ORDER_BUTTON).click()

    @allure.step('Нажать на кнопку "Заказать" в нижней части страницы')
    def click_bottom_order_button(self):
        return self.find_element(Locators.BOTTOM_ORDER_BUTTON).click()

    @allure.step('Перейти на страницу Яндекса')
    def click_yandex_button(self):
        yandex_button = self.find_element(BasePageLocator.YANDEX_SITE_BUTTON)
        yandex_button.click()

    @allure.step('Переключиться на вкладку браузера')
    def switch_window(self, window_number: int = 1):
        return self.driver.switch_to.window(self.driver.window_handles[window_number])

    def wait_url_until_not_about_blank(self, time=10):
        return WebDriverWait(self.driver, time).until_not(ec.url_to_be('about:blank'))

    @allure.step('Нажать на вопрос в "Вопросы о важном"')
    def click_faq_question(self, question_number: int):
        elems = self.find_elements(Locators.FAQ_BUTTONS, 10)
        return elems[question_number].click()

    @allure.step('Принять куки нажав на кнопку "да все привыкли"')
    def click_cookie_accept(self):
        return self.find_element(BasePageLocator.COOKIE_ACCEPT_BUTTON).click()

    @allure.step('Переключиться на новую вкладку и проверить URL')
    def switch_to_new_window_and_check_url(self, expected_url_part):
        WebDriverWait(self.driver, 10).until(ec.number_of_windows_to_be(2))  # Ждем, пока откроется новая вкладка
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])  # Переключаемся на новую вкладку
        WebDriverWait(self.driver, 10).until(lambda d: expected_url_part in d.current_url)  # Ждем, пока URL не изменится

    @allure.step('Ожидание загрузки страницы с ожидаемой частью URL')
    def wait_for_url(self, expected_url_part, timeout=10):
        WebDriverWait(self.driver, timeout).until(lambda d: expected_url_part in d.current_url)  # Ждем, пока в URL появится expected_url_part
