from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import os

from utils.preprocessing import preprocess_image, CLASS_NAMES


# --------------------------------------------------
# Flask Application
# --------------------------------------------------

app = Flask(__name__)


# --------------------------------------------------
# Model Configuration
# --------------------------------------------------

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "model",
    "cifar10_cnn_model.keras"
)


# --------------------------------------------------
# Load Trained Deep Learning Model
# --------------------------------------------------

try:
    model = load_model(MODEL_PATH)
    print("Model loaded successfully.")
except Exception as e:
    model = None
    print(f"Error loading model: {e}")


# --------------------------------------------------
# Home Endpoint
# --------------------------------------------------

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "CIFAR-10 Deep Learning Prediction API",
        "status": "API is running",
        "model": "cifar10_cnn_model.keras",
        "endpoint": "/predict",
        "method": "POST"
    })


# --------------------------------------------------
# Health Check Endpoint
# --------------------------------------------------

@app.route("/health", methods=["GET"])
def health():
    if model is not None:
        return jsonify({
            "status": "healthy",
            "model_loaded": True
        }), 200

    return jsonify({
        "status": "unhealthy",
        "model_loaded": False
    }), 500


# --------------------------------------------------
# Prediction Endpoint
# --------------------------------------------------

@app.route("/predict", methods=["POST"])
def predict():

    # Check whether model loaded
    if model is None:
        return jsonify({
            "error": "Model could not be loaded."
        }), 500

    # Check whether image is present
    if "image" not in request.files:
        return jsonify({
            "error": "No image provided.",
            "message": "Please upload an image using the 'image' field."
        }), 400

    file = request.files["image"]

    # Check filename
    if file.filename == "":
        return jsonify({
            "error": "No image selected."
        }), 400

    try:

        # Open image
        image = Image.open(file.stream)

        # Preprocess image
        processed_image = preprocess_image(image)

        # Generate prediction
        predictions = model.predict(processed_image, verbose=0)

        # Get predicted class
        predicted_index = int(np.argmax(predictions[0]))

        predicted_class = CLASS_NAMES[predicted_index]

        # Get confidence
        confidence = float(predictions[0][predicted_index])

        # Get all class probabilities
        probabilities = {
            CLASS_NAMES[i]: float(predictions[0][i])
            for i in range(len(CLASS_NAMES))
        }

        return jsonify({
            "success": True,
            "prediction": predicted_class,
            "class_index": predicted_index,
            "confidence": round(confidence * 100, 2),
            "probabilities": probabilities
        }), 200

    except Exception as e:

        return jsonify({
            "success": False,
            "error": "Prediction failed.",
            "details": str(e)
        }), 500


# --------------------------------------------------
# Error Handlers
# --------------------------------------------------

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Endpoint not found.",
        "message": "Please check the API URL."
    }), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        "error": "Method not allowed.",
        "message": "Please use the correct HTTP method."
    }), 405


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        "error": "Internal server error."
    }), 500


# --------------------------------------------------
# Run Flask Application
# --------------------------------------------------

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )