import streamlit as st
import requests
from PIL import Image
import io

# URL of the FastAPI backend (assuming it's running locally on port 8080)
API_URL = "http://localhost:8080/predict"

st.title("Garbage Classification App")

# Section to upload an image
st.header("Upload an Image")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# If an image is uploaded
if uploaded_file is not None:
    # Display the uploaded image
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image', use_column_width=True)
    
    # Convert the image to bytes
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes = img_bytes.getvalue()
    
    # Button to trigger prediction
    if st.button('Predict'):
        # Send image to FastAPI for prediction
        response = requests.post(API_URL, files={"file": img_bytes})
        
        if response.status_code == 200:
            # Display the prediction result
            prediction = response.json().get("prediction")
            st.success(f"Prediction: {prediction}")
        else:
            st.error("Failed to get a prediction. Please try again.")
