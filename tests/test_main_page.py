from helpers.urls import Urls
from pages.main_page import ScooterMainPage
from pages.order_page import ScooterOrderPage
import allure


@allure.parent_suite('Главная страница')
@allure.suite('Домашняя страница')
class TestScooterMainPage:

    @allure.title('Нажатия на кнопку "Заказать" в header.')
    @allure.description('Проверка что, на домашней странице в header по кнопке "Заказать", '
                        'просходит корректный переход на страницу "Оформления заказа".')
    def test_click_top_order_button_show_order_page(self, driver):
        scooter_main_page = ScooterMainPage(driver)
        scooter_main_page.go_to_site()
        scooter_main_page.click_cookie_accept()
        scooter_main_page.click_top_order_button()
        assert scooter_main_page.current_url() == Urls.ORDER_PAGE

    @allure.title('Нажатие на кнопку "Заказать", в блоке "Как это работает".')
    @allure.description('Проверка что, на домашней странице в блоке "Как это работает" по кнопке "Заказать", '
                        'просходит корректный переход на страницу "Оформления заказа".')
    def test_click_bottom_order_button_show_order_page(self, driver):
        scooter_main_page = ScooterMainPage(driver)
        scooter_main_page.go_to_site()
        scooter_main_page.click_cookie_accept()
        scooter_main_page.click_bottom_order_button()
        assert scooter_main_page.current_url() == Urls.ORDER_PAGE

    @allure.title('При нажатии на лого "Яндекс" происходит редирект на страницу "ЯндексДзен"')
    @allure.description('Проверка, что на домашней странице в header по кнопке "Яндекс" '
                        'происходит корректный редирект на страницу "ЯндексДзен".')
    def test_click_yandex_button_go_to_yandex(self, driver):
        scooter_main_page = ScooterMainPage(driver)
        scooter_main_page.go_to_site()
        scooter_main_page.click_cookie_accept()
        scooter_main_page.click_yandex_button()
        scooter_main_page.switch_to_new_window_and_check_url(Urls.YANDEX_HOME_PAGE)
        scooter_main_page.wait_for_url(Urls.YANDEX_PASSPORT)
        scooter_main_page.wait_for_url(Urls.DZEN_HOME_PAGE)

    @allure.title('При нажатии на лого "Самокат" происходит переход на главную страницу "ЯндексСамокат"')
    @allure.description('Проверка что, на странице "Оформления заказа"  в header по кнопке "Самокат" '
                        'происходит переход  на главную страницу "ЯндексСамокат".')
    def test_click_scooter_button_go_to_main_page(self, driver):
        scooter_main_page = ScooterMainPage(driver)
        scooter_main_page.go_to_site()
        scooter_main_page.click_cookie_accept()
        scooter_main_page.click_top_order_button()
        scooter_order_page = ScooterOrderPage(driver)
        scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        scooter_order_page.click_scooter_button()
        current_url = scooter_main_page.current_url()

        assert Urls.MAIN_PAGE in current_url
