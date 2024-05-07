# API HTTP Basics

An API provides an abstracted entry point to query our model through HTTP requests.

### HTTP methods:
- **GET**: retrieve an existing resource (read-only).
- **POST**: Create a new resource/send info.
- **PUT**: Update an existing resource.
- **PATCH**: Partially update an existing resource.
- **DELETE**: Delete a resource.

The API will respond with the request and an HTTP status code (request, code).

### HTTP status code:
- **2xx**: Successful operation.
- **3xx**: Redirect.
- **4xx**: Client Error.
- **5xx**: Server Error.

APIs can be implemented in Python using `Django`, `Flask` & `FastAPI`.