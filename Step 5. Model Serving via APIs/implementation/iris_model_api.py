"""
----------------------------------------------------------------------------------------------
iris_model_api.py

Develop the API to serve the iris model.

: 06 May 24
: zachcolinwolpe@gmail.com
----------------------------------------------------------------------------------------------
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib


# 1. Load the model
rf = joblib.load("iris_rf.joblib")


# 2. define the input data class
class InputData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


# 3. Create the FastAPI app
app = FastAPI()

# 4. Create the API endpoint
@app.post("/predict", response_model=dict)
async def predict(data: InputData):
    try:
        # 5. Prepare the input data
        sample = pd.DataFrame(data.dict(), index=[0])
        # 6. Make a prediction
        prediction = rf.predict(sample)
        return {"prediction": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 
