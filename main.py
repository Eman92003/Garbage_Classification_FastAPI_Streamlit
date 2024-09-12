from fastapi import FastAPI, File, UploadFile
from io import BytesIO
from PIL import Image
from model import predict_image
from funcs import preprocess_image
import uvicorn
# Initialize the FastAPI app

app = FastAPI()

@app.get('/')
def home():
    return {"health_check":'ok'}

# Endpoint to handle image uploads and predictions
@app.post("/predict/")
async def predict(file: UploadFile = File(...)):

    # Endpoint to predict the class of an uploaded image.
    # Read the image file
    contents = await file.read()
    img = Image.open(BytesIO(contents))

    # Preprocess the image
    img_array = preprocess_image(img)

    # Perform prediction using the loaded model
    prediction = predict_image(img_array)

    # Return only the top predicted label
    return {"prediction": prediction}


