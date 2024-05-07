# Why Use `POST` Instead of `GET` (HTTP Request)

The choice between using a POST request instead of a GET request for the predict endpoint is primarily due to the following reasons:

1. **Data Size**: GET requests are not suitable for sending large amounts of data because data is sent in the URL. It is not practical to send lengthy texts or large payloads as URL parameters due to URL length limitations and readability issues.

2. **Security**: GET requests can be cached and remain in browser history. If you are dealing with sensitive data, it's safer to use POST requests as they do not remain in the browser history and are not cached by default.

3. **Semantics**: According to HTTP method definitions, GET requests should be used for retrieving data without affecting the data on the server. POST requests, on the other hand, are used to submit data to the server and can result in changes in server state or side effects (like logging a transaction). In the case of a prediction API, although you're technically "retrieving" predictions, you're submitting data for processing, which aligns more closely with the intended use of POST.
These reasons make POST the more appropriate choice for operations like making predictions where potentially large amounts of data are submitted to the server for processing.