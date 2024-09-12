from tensorflow.keras.models import load_model
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np


# Load the saved model (don't forget to change the name)
model = load_model('model_resnet_50.h5')

classes = [
 'battery',
 'biological',
 'brown-glass',
 'cardboard',
 'clothes',
 'green-glass',
 'metal',
 'paper',
 'plastic',
 'shoes',
 'trash',
 'white-glass'
]

def predict_image(image_array):
    #Predict the label of the image using the loaded model.
    
    # Perform prediction using the loaded model
    preds = model.predict(image_array)
    
    # Decode predictions to human-readable labeltext 
    #decoded_preds = decode_predictions(preds, top=3)[0]
    predicted_class_idx = np.argmax(preds, axis=1)[0]
    
    # Map the index to the corresponding class
    predicted_class = classes[predicted_class_idx]

    # Return only the top predicted label
    return predicted_class
