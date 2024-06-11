# Тестовое задание.

## Описание проекта
Api для получения информации об объявлениях по ссылке.

## Стэк технологий
![Python 3.9](https://img.shields.io/badge/Python-3.9-blue.svg)
![Django 3.2.16](https://img.shields.io/badge/Django-3.2.16-green.svg)
![djangorestframework
3.12.4](https://img.shields.io/badge/djangorestframework-3.12.4-green)

## Другие пакеты и библиотеки
Включены в requirements.txt. Адрес: test_case/requirements.txt

### Как запустить проект: 
Клонируйте репозиторий:

```bash
git clone https://github.com/kise2k/test_api_solution.git
```
Перейдите в него в командной строке:

```bash
cd test_case
```

Cоздайте и активируйте виртуальное окружение:

```bash
python3 -m venv venv 
```

Установите зависимости
```bash
source venv/Scripts/activate
```

Обновите pip и установите зависимости: каждая команда - отдельно
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Алгоритм регистрации пользователя:

1. Пользователь отправляет POST-запрос на добавление нового пользователя с параметрами username и password на эндпоинт /auth/users/.
2. Затем пользователь отправляет POST-запрос на получения токена с параметрами username и password на эндпоинт /auth/token/login/.
3. Чтобы получить доступ к защищенным маршрутам нужно передавать токен вместе с запросом.

## Примеры запросов и ответов

GET-запрос на эндпойнт 
```bash
http://127.0.0.1:8000/api/ads
```
дает следующий ответ:
```bash
{
    "count": 10,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 13,
            "title": "Установка видеонаблюдения и домофонии",
            "views": 750,
            "author": "Primtec",
            "position": 1
        },
        {
            "id": 14,
            "title": "Установка и монтаж систем видеонаблюдения",
            "views": 379,
            "author": "VKSystem",
            "position": 2
        },
        {
            "id": 15,
            "title": "Установка видеонаблюдения и видеокамер в домах во Владивостоке",
            "views": 1716,
            "author": "ООО \"Тесла\"",
            "position": 3
        },
        {
            "id": 16,
            "title": "Монтаж и обслуживание систем видеонаблюдения, СКУД, домофоны во Владивостоке",
            "views": 347,
            "author": "Videofort",
            "position": 4
        },
        {
            "id": 17,
            "title": "Монтаж видеонаблюдения Hikvision HiWatch Trassir, СКУД, домофонов во Владивостоке",
            "views": 439,
            "author": "doneit",
            "position": 5
        },
        {
            "id": 18,
            "title": "Продажа и установка видеонаблюдения. Монтаж любой сложности! Гарантия во Владивостоке",
            "views": 3856,
            "author": "Точка-Видео",
            "position": 6
        },
        {
            "id": 19,
            "title": "Видеонаблюдение Установка Продажа Настройка Видеокамер IP во Владивостоке",
            "views": 1398,
            "author": "TVi MART",
            "position": 7
        },
        {
            "id": 20,
            "title": "Установка камер, обслуживание, монтаж видеонаблюдения и домофонов во Владивостоке",
            "views": 48,
            "author": "SergeyLevchenko",
            "position": 8
        },
        {
            "id": 21,
            "title": "ВидеоКИТ - Системы видеонаблюдения, установка, обслуживание во Владивостоке",
            "views": 120,
            "author": "VideoKIT",
            "position": 9
        },
        {
            "id": 22,
            "title": "Установим Видеодомофон в квартиру или частный дом! Видеонаблюдение во Владивостоке",
            "views": 77,
            "author": "Подряд",
            "position": 10
        }
    ]
}
```

GET-запрос на эндпойнт 
```bash
http://127.0.0.1:8000/api/ads/13
```

дает следующий ответ:
```bash
{
    "id": 13,
    "title": "Установка видеонаблюдения и домофонии",
    "views": 750,
    "author": "Primtec",
    "position": 1
}
```
