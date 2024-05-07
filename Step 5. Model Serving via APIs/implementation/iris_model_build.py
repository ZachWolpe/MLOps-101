"""
----------------------------------------------------------------------------------------------
iris_model_build.py

Setup an iris model for demonstration purposes.

: 06 May 24
: zachcolinwolpe@gmail.com
----------------------------------------------------------------------------------------------
"""

# 1. Library imports
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from pydantic import BaseModel
import joblib


# 2. Class which describes a single flower measurements
class IrisSpecies(BaseModel):
    sepal_length: float 
    sepal_width: float 
    petal_length: float
    petal_width: float


# 3. Load the iris dataset
iris = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# 4. Train a random forest classifier
X = iris.drop(columns=["species"])
y = iris["species"]
rf = RandomForestClassifier()
rf.fit(X, y)

# 5. Save the model
joblib.dump(rf, "iris_rf.joblib")
