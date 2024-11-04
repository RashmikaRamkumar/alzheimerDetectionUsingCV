# Alzheimer Disease Detection Application

This project is a web application designed to assist in the prediction of Alzheimer's Disease using image classification. The model leverages Convolutional Neural Networks (CNN) for image-based prediction, making it a useful tool in the preliminary stages of Alzheimer’s diagnosis.

## Table of Contents

- [Overview](#overview)
- [About Alzheimer's Disease](#about-alzheimers-disease)
- [Approach: Computer Vision and CNN](#approach-computer-vision-and-cnn)
- [Application Structure and Functionality](#application-structure-and-functionality)
- [How to Run the Application](#how-to-run-the-application)
- [Future Enhancements](#future-enhancements)
- [Acknowledgements](#acknowledgements)

## Overview

The Alzheimer Disease Detection application takes an MRI or CT scan image as input and uses a trained CNN model to classify it into different stages of Alzheimer's Disease. This provides clinicians and researchers with a valuable, quick, and accurate tool for understanding a patient's condition.

The application is built with:

- **Frontend**: React (Upload Form for image selection)
- **Backend**: Flask API (for handling image uploads and predictions)
- **Model**: CNN model trained in Python using TensorFlow/Keras

## About Alzheimer’s Disease

Alzheimer’s Disease (AD) is a progressive neurological disorder that affects memory, cognitive abilities, and behavior. Symptoms include memory loss, confusion, disorientation, and eventually, loss of bodily functions.

There are four commonly classified stages of Alzheimer’s:

1. **Normal**: No signs of Alzheimer's in brain scans.
2. **Very Mild Cognitive Impairment (MCI)**: Minor memory issues that do not impact daily functioning.
3. **Mild Cognitive Impairment**: Noticeable memory, thinking, and language issues.
4. **Moderate Cognitive Impairment**: Significant memory loss, requiring assistance with daily tasks.

Early detection and intervention can help slow down the disease's progression and improve the quality of life for those affected.

## Approach: Computer Vision and CNN

### Computer Vision in Medical Imaging

Computer Vision (CV) techniques allow us to analyze medical images for patterns and anomalies. In this application, we use CV to interpret brain scan images, detecting areas associated with Alzheimer’s.

### Convolutional Neural Network (CNN)

CNNs are particularly effective for image classification tasks because they learn spatial hierarchies in images through layers of convolutions, pooling, and activation functions. Our CNN model has been trained to detect specific features related to Alzheimer’s Disease stages:

- **Convolutional Layers** extract essential features from brain scan images.
- **Pooling Layers** reduce the spatial dimensions, retaining the most critical information.
- **Fully Connected Layers** interpret these extracted features to predict the Alzheimer’s stage.

The model has been trained and validated on a labeled dataset of brain images to achieve high accuracy in classifying the stages of Alzheimer’s.

### Model Training Process

The model training involved the following steps:

1. **Data Collection**: Collect MRI or CT scans of brain images labeled by Alzheimer’s stage.
2. **Data Preprocessing**: Resize images, apply image augmentation, and normalize pixel values.
3. **Model Architecture Design**: Configure layers, including convolution, pooling, and fully connected layers.
4. **Training**: Train the model on labeled data, optimizing weights to minimize error.
5. **Validation**: Test the model with unseen data to evaluate accuracy.

## Application Structure and Functionality

The application contains:

- **UploadForm.jsx**: A React component allowing users to select and upload an image.
- **Flask Backend**: Receives the image file, runs it through the model, and returns the predicted stage of Alzheimer’s.

### Key Files and Directories

- `src/components/UploadForm.jsx`: Frontend component for image selection and upload.
- `src/style.css`: Styling for the application.
- `app.py`: Flask API backend that handles image prediction requests.
- `model.h5`: Trained CNN model for Alzheimer’s stage classification.

## How to Run the Application

### Setup Backend (Flask)

1. **Create a Virtual Environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`


2. **Navigate to the Backend Directory**

   ```bash
   cd backend
3. **Install Python Dependencies**

   ```bash
   pip install -r requirements.txt

4. **Run the Flask Server**
   ```bash
   python app.py

The Flask API will be running on http://127.0.0.1:5000.

### Setup Frontend (React)

1. **Navigate to the Frontend Directory**
     ```bash
   cd frontend

3. **Install Node.js Dependencies**
    ```bash
   npm install
   

5. **Start the React Application**
   ```bash
   npm run dev
The React application will be available at http://localhost:5173.





