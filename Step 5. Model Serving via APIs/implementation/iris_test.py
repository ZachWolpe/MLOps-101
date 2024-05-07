"""
----------------------------------------------------------------------------------------------
iris_test.py

Test the iris model API.

: 06 May 24
: zachcolinwolpe@gmail.com
----------------------------------------------------------------------------------------------
"""

import requests

# 1. Define the API endpoint
url = "http://127.0.0.1:8000/predict"

# 2. Define the input data
new_iris_measurements = {
    'sepal_length': 5.7,
    'sepal_width': 3.1,
    'petal_length': 4.9,
    'petal_width': 2.2
}


# 3. Make a request to the API
if __name__ == '__main__':
    response = requests.post('http://127.0.0.1:8000/predict',
                             json=new_iris_measurements)
    print(response.content)
