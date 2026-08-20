from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd  # <-- ADD THIS

# Load the trained model
model = joblib.load('model.joblib')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class SensorData(BaseModel):
    vibration: float
    temperature: float
    pressure: float
    load: float
#Predict end-point
@app.post("/predict")
async def predict(data: SensorData):
    # Create a DataFrame with proper column names
    input_df = pd.DataFrame([[
        data.vibration, 
        data.temperature, 
        data.pressure, 
        data.load
    ]], columns=['vibration', 'temperature', 'pressure', 'load'])
    
    # Predict using the DataFrame
    risk_probability = model.predict_proba(input_df)[0][1]
    
    return {"risk": round(risk_probability * 100, 1)}