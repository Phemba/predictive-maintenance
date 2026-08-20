#Imports
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib


# Generating fake sensors data (1000 samples)

np.random.seed(42)
n = 1000
vibration = np.random.uniform(0,10,n)
temperature = np.random.uniform(20,100,n)
pressure = np.random.uniform(0,150,n)
load = np.random.uniform(0,100,n)

#Creating fake "failure" column(5% failure rate)
failure_prob = (vibration/10* 0.5 + temperature/100*0.3 + pressure/150*0.1 + load/100*0.1) 
failure = (np.random.random(n) < failure_prob *0.3).astype(int)

#Creating DataFrame
df = pd.DataFrame({
    'vibration': vibration,
    'temperature': temperature,
    'pressure': pressure,
    'load': load,
    'failure': failure
})

#Training the Model

X = df[['vibration','temperature','pressure','load']]
y = df['failure']
model = RandomForestClassifier(n_estimators=100,max_depth=3,random_state=42)
model.fit(X,y) 

#Save Model
joblib.dump(model,'model.joblib')
print("Model trained and saved!")
