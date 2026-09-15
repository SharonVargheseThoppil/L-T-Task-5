# Task 5: API Testing and Validation using Postman/Curl

## L&T EduTech – Deep Learning Task Series

This project contains the testing and validation implementation for the **CIFAR-10 Deep Learning Prediction API** developed using Flask in Task 4.

The API is tested using **Postman** and **Curl** to verify API availability, prediction functionality, JSON responses, negative inputs, and error-handling behaviour.

---

## Objective

To validate and test a deep learning prediction API using industry-standard API testing tools such as **Postman** and **Curl**.

---

## Tools and Technologies Used

* Python 3.12.8
* Flask
* TensorFlow / Keras
* Postman
* Curl
* CIFAR-10 Dataset
* JSON
* REST API

---

## API Under Test

The Flask application provides the following endpoints:

| Method | Endpoint   | Purpose                                          |
| ------ | ---------- | ------------------------------------------------ |
| GET    | `/`        | Check API availability                           |
| POST   | `/predict` | Upload an image and obtain a CIFAR-10 prediction |

### Base URL

```text
http://127.0.0.1:5000
```

### Prediction Request

The `/predict` endpoint accepts an image using:

```text
multipart/form-data
```

The form-data field name is:

```text
image
```

---

## Project Structure

```text
Task 5 API Testing and Validation using Postman_curl/
│
├── README.md
├── requirements.txt
├── app.py
├── Task 5 - CIFAR-10 API Testing.postman_collection.json
├── cnn_cifar10_model.keras
└── test/
    └── sample_images/
        └── test_image.jpg
```

> The exact files included in the repository may depend on the final project submission structure.

---

## Testing Performed

The following test scenarios were performed using Postman:

### Positive Testing

**TC01 – API Availability**

* Method: `GET`
* Endpoint: `/`
* Expected Status: `200 OK`
* Purpose: Verify that the Flask API is running.

**TC02 – Valid Prediction**

* Method: `POST`
* Endpoint: `/predict`
* Input: Valid image file
* Expected Status: `200 OK`
* Purpose: Verify successful image prediction.

**TC03 – JSON Response Validation**

* Method: `POST`
* Endpoint: `/predict`
* Purpose: Validate HTTP status and JSON response format using Postman test scripts.

### Negative Testing

**TC04 – Missing Image Input**

Tests the API behaviour when no image is provided.

**TC05 – Invalid Input Type**

Tests the API using an invalid file type instead of a valid image.

**TC06 – Empty Input**

Tests the prediction endpoint without providing the required input.

**TC07 – Invalid Endpoint**

Tests a non-existent API endpoint to verify 404 error handling.

---

## JSON Response Validation

The successful prediction response contains information such as:

```json
{
    "class_index": 5,
    "confidence": 99.99,
    "prediction": "dog",
    "probabilities": {},
    "success": true
}
```

The response structure is validated using Postman assertions.

Example assertions include:

```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Response is JSON", function () {
    pm.response.to.be.json;
});
```

---

## Curl Testing

Curl was also used as an independent cross-check of the Flask API.

Example API availability request:

```bash
curl http://127.0.0.1:5000/
```

Example prediction request:

```bash
curl -X POST -F "image=@test_image.jpg" http://127.0.0.1:5000/predict
```

---

## Test Results

The testing covered:

* API availability
* Successful prediction
* JSON response validation
* Missing input
* Invalid input type
* Empty input
* Invalid endpoint
* Curl-based verification

The observed results showed successful responses for the majority of test cases.

The invalid input type test returned a `500 Internal Server Error` rather than a client-side `400`-class response. This behaviour was documented as a limitation and indicates that the API could be improved by handling invalid image files more explicitly.

---

## Key Observations

1. The API was accessible through the local Flask server.
2. The prediction endpoint successfully processed a valid image.
3. Successful responses were returned in JSON format.
4. Postman assertions successfully validated the HTTP status and JSON response.
5. Missing and empty inputs were handled with `400 Bad Request`.
6. Invalid endpoints returned `404 Not Found`.
7. Invalid file input resulted in a `500 Internal Server Error`, highlighting an area for improved error handling.
8. Curl provided an independent verification of the API behaviour.

---

## How to Run the Project

### 1. Create and activate the virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

### 3. Start the Flask API

```powershell
python app.py
```

The API should be available at:

```text
http://127.0.0.1:5000
```

### 4. Test using Postman

Open the supplied Postman collection:

```text
Task 5 - CIFAR-10 API Testing.postman_collection.json
```

Run the requests against the local Flask API.

---

## Deliverables

This repository contains the materials associated with Task 5:

* API testing report
* Postman collection
* Source code
* Requirements file
* Supporting project files

The API testing report contains detailed test cases, response logs, screenshots, observations, and conclusions.

---

## Limitations

The testing was performed on a local Flask instance and focused on the defined test scenarios.

The testing does not represent comprehensive performance or security testing. Areas such as high-concurrency testing, large-payload testing, and extensive load testing were outside the scope of this task.

---

## Conclusion

Task 5 validates the CIFAR-10 Flask prediction API using Postman and Curl. The testing verifies API availability, prediction functionality, JSON response validation, negative testing, and error-handling behaviour.

The results and observations are documented in the accompanying API Testing and Validation Report.

---

## Author

**Sharon Varghese Thoppil**

**Programme:** Deep Learning from Production to Deployment

**Institution:** B.K. Birla College

**L&T EduTech – Deep Learning Task Series**

