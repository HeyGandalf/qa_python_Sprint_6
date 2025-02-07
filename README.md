# Проект автоматизации тестирования сайта

https://qa-scooter.praktikum-services.ru/

## Описание

Этот проект содержит автоматизированные тесты для сайта ЯндексСамокат с использованием Python, Selenium и других инструментов. Тесты покрывают основные сценарии пользовательского взаимодействия с сайтом, включая проверку работы кнопок, переходов и редиректов, а также взаимодействие с cookies и вкладками браузера.

## Технологии

- Python 3.9
- Selenium
- pytest
- Allure
- WebDriver (для браузера Chrome/Firefox)
- Pytest-Allure plugin для генерации отчетов

## Структура

Sprint_6/
│
├── helpers/
│   ├── data.py
│   ├── locators.py
│   ├── urls.py
│
├── pages/
│   ├── base_page.py
│   ├── main_page.py
│   ├── order_page.py
│
├── tests/
│   ├── test_main_page.py
│
├── conftest.py
├── allure_results/
├── README.md
└── pytest.ini

В папке helpers хранятся вспомогательные файлы: data.py, locators.py и urls.py.
В папке pages находятся файлы с описанием страниц.
Файл conftest.py в корневой папке для конфигурации и настройки окружения.
Результаты Allure сохраняются в папке allure_results.


## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/HeyGandalf/qa_python_Sprint_6
    ```
2. Перейдите в каталог проекта:
    ```bash
    cd Sprint_6
    ```
3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

## Запуск тестов

Чтобы запустить тесты, выполните следующую команду:
```bash
pytest --alluredir=allure_results


