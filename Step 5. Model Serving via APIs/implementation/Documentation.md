
# Serving Models through an API

## Step 1. Build the Model

Two models are built in this example. Run the files suffixed with `_model.py` to build the models.

- [X] Hugging Face Model: a sentiment analysis model, built using the Hugging Face Transformers library & Tensorflow.
- [X] Iris Model: a random forrest classfier model (Keras) trained on the iris dataset.

```bash
python hugging_face_model.py
python iris_model.py
```

## Step 2. Serve the Models

The API logic to serve the models is in the files suffixed with `_api.py`. Run the files to start the API server.

```bash
fastapi run hugging_face_api.py
```

```bash
fastapi run iris_api.py
```

Alternatively, run the model in dev mode:
    
```bash
fastapi dev hugging_face_api.py
```

```bash
fastapi dev iris_api.py
```

## Step 3. Test the API

The API server is now running on local host `http://127.0.0.1:8000`. You can query the API on local host using the Swagger UI.

Swagger also provides `cURL` code snippets to test the API.



Run a request from the command line using cURL.

```curl
curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "string"
}'
```

alternatively, use make a request using Python in the `_test.py` files.

```bash
python hugging_face_test.py
```

or
```bash
python iris_test.py
```


