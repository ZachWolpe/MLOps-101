"""
----------------------------------------------------------------------------------------------
hugging_face_test.py

Test the hugging face API.

: 06 May 24
: zachcolinwolpe@gmail.com
----------------------------------------------------------------------------------------------
"""

import requests

# 1. Define the API endpoint
url = "http://127.0.0.1:8000/predict"

# 2. Define the input data
new_text = {
    'text': "I am very happy with the financial results of the company."
}

# 3. Make a request to the API
if __name__ == '__main__':
    response = requests.post('http://127.0.0.1:8000/predict',
                             json=new_text)
    print(response.content)
