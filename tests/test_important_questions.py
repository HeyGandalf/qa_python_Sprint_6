import pytest
import allure
from pages.main_page import ScooterMainPage
from helpers.data import ScooterMainPageFAQ
from helpers.locators import ScooterMainPageLocator


@allure.parent_suite('Главная страница')
@allure.suite('Вопросы о важном')
class TestScooterFAQPage:
    @allure.title('При нажатии на вопрос раскрывается ответ ')
    @allure.description('Проверка что при нажатии на поле вопроса в блоке "Вопросы о важном", '
                        'данный вопрос раскрывается и текст в нем соответствует ОР')
    @pytest.mark.parametrize(
        "question,answer,expected_answer",
        [
            (0, 0, ScooterMainPageFAQ.answer1),
            (1, 1, ScooterMainPageFAQ.answer2),
            (2, 2, ScooterMainPageFAQ.answer3),
            (3, 3, ScooterMainPageFAQ.answer4),
            (4, 4, ScooterMainPageFAQ.answer5),
            (5, 5, ScooterMainPageFAQ.answer6),
            (6, 6, ScooterMainPageFAQ.answer7),
            (7, 7, ScooterMainPageFAQ.answer8),
        ]
    )
    def test_faq_click_first_question_show_answer(self, driver, question, answer, expected_answer):
        scooter_main_page = ScooterMainPage(driver)
        scooter_main_page.go_to_site()
        scooter_main_page.click_cookie_accept()
        scooter_main_page.click_faq_question(question_number=question)
        answer = scooter_main_page.find_element(ScooterMainPageLocator.faq_answer(answer_number=answer))

        assert answer.is_displayed() and answer.text == expected_answer, 'Ответ на вопрос не совпадает с ожидаемым ' \
                                                                         'значением'
