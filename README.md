# Chicago apartment rent price prediction: Web Scraping - Machine Learning - Deploy

## Задача проекта

Цель проекта — разработка модели для предсказания цен на аренду квартир в Чикаго.

## План исследования

1. Сбор данных с сайта по аренде квартир с помощью [веб-скрапинга] (https://github.com/elenadigital/Chicago_apartment_rent_price_prediction_Web_Scraping_Machine-Learning_Deploy/blob/main/web_scrapping_apartmentguide.ipynb)
2. Импорт библиотек и загрузка данных
3. Предобработка данных
4. Исследовательский анализ данных:
    - Анализ числовых признаков
    - Анализ категориальных значений
    - Соотношение признаков с целевой переменной price
5. Обучение базовых моделей (Baseline)
6. Тюнинг моделей:
    - Создание новых признаков
        - crime_nearby — количество зарегистрированных преступлений в непосредственной близости от квартиры;
        - crime_density_level — уровень преступности в районе расположения квартиры;
        - distance_to_center_miles — расстояние до центра Чикаго (в милях)
    - Проверка значений на мультиколлинеарность
    - Проверка важности признаков (Mutual Information)
    - Отбор признаков
    - Оптимизация моделей с использованием Pipeline и GridSearchCV
7. Финальное предсказание на тестовой выборке
8. Проверка важности признаков (Feature Importances)
9. Проверка модели на новых данных
10. Настройка API и контейнеризация проекта в Docker

## Решение

Были обучены 3 модели:

- Linear Regression
- Random Forest
- CatBoost

Модель CatBoost показала лучший результат:
- на тренировочной выборке MAE ~290, RMSE ~508, R² ~0.75
- на тестовой выборке MAE ~306, RMSE ~840, R² ~0.67

Наибольший вклад в предсказания модели внесли признаки:

- baths
- distance_to_center_miles
- beds
- latitude

Таким образом, ключевыми факторами стоимости аренды оказались комфорт квартиры (baths, beds) и её расположение (distance_to_center_miles, latitude). CatBoost стала оптимальной моделью для предсказания цен: она показала высокую точность, устойчивость к переобучению и адекватно справилась с вариативностью данных. Модель готова к применению на новых данных и для анализа рынка аренды квартир в Чикаго.

## Инструкция по запуску проекта

1. Клонируйте репозиторий:

git clone https://github.com/elenadigital/Chicago_apartment_rent_price_prediction_Web_Scraping_Machine-Learning_Deploy.git
cd Chicago_apartment_rent_price_prediction_Web_Scraping_Machine-Learning_Deploy

2. Соберите образ Docker:

docker build -t chicago-apartment-rent-price-prediction-service:latest .

3. Запустите контейнер:

docker run -d -p 8000:5000 chicago-apartment-rent-price-prediction-service:latest

4. Проверьте API:

Откройте в браузере: http://localhost:8000/

**Доступные endpoints:**

* GET /health — проверить, работает ли API

* GET /stats — получить статистику по числу запросов

* POST /predict — сделать предсказание

## Используемые библиотеки и инструменты

Beautifulsoup4, Requests, Selenium, Undetected-Chromedriver, Pandas, NumPy, Matplotlib, Seaborn, Scipy, Folium, Phik, Sklearn, CatBoost, Pickle, FastAPI, Docker
