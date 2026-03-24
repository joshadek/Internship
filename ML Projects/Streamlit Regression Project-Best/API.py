from fastapi import FastAPI
import uvicorn
import joblib
from pydantic import BaseModel
import numpy as np

model = joblib.load("California_homesXGB.pkl")

app = FastAPI(
    title="California Housing Price Predictor",
    description="Predicts median house value using Linear Regression",
    version="1.0"
)

class HouseFeatures(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

@app.get("/")
def root():
    return {"status": "API is running"}

@app.post("/predict")
def predict(features: HouseFeatures):
    input_data = np.array([[
        features.MedInc,
        features.HouseAge,
        features.AveRooms,
        features.AveBedrms,
        features.Population,
        features.AveOccup,
        features.Latitude,
        features.Longitude
    ]])

    prediction = model.predict(input_data)[0]

    return {
        "predicted_median_house_value": round(float(prediction), 4),
        "unit": "hundreds of thousands of USD"
    }

if __name__ == "__main__":
    uvicorn.run("API:app", host="0.0.0.0", port=8000, reload=True)