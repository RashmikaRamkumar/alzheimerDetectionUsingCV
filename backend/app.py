from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import os
from flask_cors import CORS
import cv2

app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "http://localhost:5173"}})

# Load your trained model
model = load_model("model/alzheimer_model.h5")

# Ensure the uploads folder exists
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Define categories
categories = ["Mild Demented", "Moderate Demented", "Non Demented", "Very Mild Demented"]

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    file = request.files['image']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Preprocess image
    img = load_img(file_path, color_mode="grayscale", target_size=(128, 128))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Get prediction
    prediction = model.predict(img_array)
    category_index = np.argmax(prediction)
    predicted_category = categories[category_index]

    # Clean up uploaded image
    os.remove(file_path)

    return jsonify({"category": predicted_category})
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Alzheimer's Disease Detection API. Use POST /predict to classify brain scans."})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
