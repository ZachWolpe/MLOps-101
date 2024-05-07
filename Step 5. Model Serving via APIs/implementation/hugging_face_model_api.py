"""
----------------------------------------------------------------------------------------------
hugging_face_model_api.py

Serve the model via an API using FastAPI.

: 06 May 24
: zachcolinwolpe@gmail.com
----------------------------------------------------------------------------------------------
"""


from transformers import AutoModelForSequenceClassification, AutoTokenizer
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import torch

# load the model & tokenizer from the local directory
model = AutoModelForSequenceClassification.from_pretrained("finbert")
tokenizer = AutoTokenizer.from_pretrained("finbert")

# create the FastAPI app
app = FastAPI()


# create a class for the input data
class InputData(BaseModel):
    text: str


# create the API endpoint
@app.post("/predict", response_model=dict)
async def predict(data: InputData):
    try:
        # tokenize the input data
        inputs = tokenizer(data.text, return_tensors="pt")
        # make a prediction
        with torch.no_grad():
            outputs = model(**inputs).logits
        # get the predicted label
        predicted_class_id = outputs.argmax().item()
        predicted_class_name = model.config.id2label[predicted_class_id]
        # return the predicted label
        return {
            'class_id': predicted_class_id,
            'class_name': predicted_class_name}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))