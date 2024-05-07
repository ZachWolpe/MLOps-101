"""
----------------------------------------------------------------------------------------------
hugging_face_model_build.py

Download the model from hugging face and store it in the local directory.

: 06 May 24
: zachcolinwolpe@gmail.com
----------------------------------------------------------------------------------------------
"""

from transformers import AutoModelForSequenceClassification, AutoTokenizer

# load from hugging face api
model_name = "ProsusAI/finbert"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# store the model & tokenizer in the local directory
model.save_pretrained("finbert")
tokenizer.save_pretrained("finbert")

# load the model & tokenizer from the local directory
model = AutoModelForSequenceClassification.from_pretrained("finbert")
tokenizer = AutoTokenizer.from_pretrained("finbert")



