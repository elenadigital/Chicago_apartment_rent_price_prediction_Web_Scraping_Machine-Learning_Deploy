'''
Реализуем API с тремя эндпоинтами:

1. POST /predict —
Для получения предсказания от модели на основе входных данных

2. GET /stats —
Для получения статистики использования API

3. GET /health —
Для проверки работоспособности API

Шаг 1: Установка необходимых библиотек
pip install fastapi uvicorn pydantic scikit-learn pandas numpy catboost

Шаг 2: Создание app_api.py
Шаг 3: Запуск приложения: python app_api.py
Шаг 4: Тестирование API

Тест API с помощью curl:

curl -X GET http://127.0.0.1:5000/health
curl -X GET http://127.0.0.1:5000/stats
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d '{
  "beds": 1,
  "baths": 1.0,
  "sqft": 452.0,
  "parking": 0,
  "latitude": 41.9214378,
  "longitude": -87.6513043,
  "postal_code": 60614,
  "pets_friendly": 1,
  "dishwasher": 1,
  "microwave": 1,
  "stainless_steel_appliances": 0,
  "gym": 0,
  "elevator": 1,
  "office_center_conference_room": 0,
  "on_site_laundry": 1,
  "hot_tub": 0,
  "pool": 0,
  "heat": 1,
  "quartz_countertops": 0,
  "crime_nearby": 3000,
  "crime_density_level": 1,
  "distance_to_center_miles": 3.5,
  "type": "apartment"
}'


'''

from fastapi import FastAPI
import pickle
import pandas as pd
from pydantic import BaseModel
import os

app = FastAPI()

# Загружаем модель
model_path = os.path.join(os.path.dirname(__file__), "best_model.pkl")
with open(model_path, "rb") as f:
    best_model = pickle.load(f)

# Счетчик запросов
request_count = 0

# Модель для валидации входных данных
class PredictionInput(BaseModel):
    beds: int
    baths: float
    sqft: float
    parking: int
    latitude: float
    longitude: float
    postal_code: int
    pets_friendly: int
    dishwasher: int
    microwave: int
    stainless_steel_appliances: int
    gym: int
    elevator: int
    office_center_conference_room: int
    on_site_laundry: int
    hot_tub: int
    pool: int
    heat: int
    quartz_countertops: int
    crime_nearby: int
    crime_density_level: int
    distance_to_center_miles: float
    type: object

@app.get("/stats")
def stats():
    return {"request_count": request_count}

@app.get("/health")
def health():
    return {"status": "OK"}

@app.post("/predict")
def predict(input_data: PredictionInput):
    global request_count, best_model
    request_count += 1

    # Преобразуем входные данные в DataFrame
    new_data = pd.DataFrame([input_data.dict()])

    # Получаем предсказание (регрессия → число)
    prediction = best_model.predict(new_data)[0]

    return {"Предсказанная цена аренды для указанной квартиры": float(prediction)}
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)

