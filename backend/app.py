from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd  

# Load the trained model
model = joblib.load('model.joblib')

app = FastAPI()

#CORS configuration to allow requests from the Angular frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_methods=["*"],
    allow_headers=["*"],
)

#This defines the exact shape of data that the API expects to receive.
class SensorData(BaseModel):
    type: int
    air_temperature: float
    process_temperature: float
    rotational_speed: float
    torque: float
    tool_wear: float
    
@app.post("/predict")
async def predict(data: SensorData):
    #The model was trained on a DataFrame with these specific columns.
    #Names (including spaces and units, e.g., "Air temperature [K]") must match exactly.
    input_df = pd.DataFrame([[
        data.type,
        data.air_temperature,
        data.process_temperature,
        data.rotational_speed,
        data.torque,
        data.tool_wear
    ]], columns=[
        'Type',
        'Air temperature [K]',
        'Process temperature [K]',
        'Rotational speed [rpm]',
        'Torque [Nm]',
        'Tool wear [min]'
    ])
    
    # predict_probabilities returns the probability for both classes: [P(no failure)]
    # we onl need the failure probability, so we take Index [1]
    
    risk_probability = model.predict_proba(input_df)[0][1]
    
    # Convert to a percentage and round 1 decimal place
    return {"risk": round(risk_probability * 100, 1)}
    