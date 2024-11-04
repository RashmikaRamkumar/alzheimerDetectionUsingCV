// src/components/UploadForm.jsx
import React, { useState } from 'react';
import axios from 'axios';

const UploadForm = () => {
    const [image, setImage] = useState(null);
    const [result, setResult] = useState('');

    const handleFileChange = (e) => {
        setImage(e.target.files[0]);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!image) return;

        const formData = new FormData();
        formData.append('image', image);

        try {
            const response = await axios.post('https://alzheimerdetectionusingcv.onrender.com/predict', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            setResult(`Predicted Category: ${response.data.category}`);
        } catch (error) {
            console.error('Error:', error);
            setResult('An error occurred while predicting the category.');
        }
    };

    return (
        <div className="upload-form">
            <h1>Alzheimer Disease Detection</h1>
            <form onSubmit={handleSubmit}>
                <input type="file" onChange={handleFileChange} accept="image/*" required />
                <button type="submit">Predict</button>
            </form>
            <div className="result">{result}</div>
        </div>
    );
};

export default UploadForm;
