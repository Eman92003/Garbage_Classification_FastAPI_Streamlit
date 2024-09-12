import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image
from tensorflow.keras.applications.resnet50 import preprocess_input

def preprocess_image(img: Image.Image) -> np.ndarray:
    # Preprocess the image for prediction.
    # Resize the image to 224x224 pixels (the input size expected by ResNet50)
    img = img.resize((384, 384))
    
    # Convert the image to a numpy array
    img_array = image.img_to_array(img)
    
    # Expand dimensions to match the shape the model expects (batch size, height, width, channels)
    img_array = np.expand_dims(img_array, axis=0)
    
    # Preprocess the input for ResNet50
    img_array = preprocess_input(img_array)
    
    return img_array
