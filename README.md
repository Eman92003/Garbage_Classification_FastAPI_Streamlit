# Image Classification Model: Deployable Deep Learning Solution

This repository provides a complete solution for garbage classification, combining a pre-trained machine learning model with an API for easy deployment and integration.

## Notebook Steps

### 1. Import Needed Libraries

### 2. Data Loading and Preprocessing
* Loads the dataset containing images of various types of garbage (e.g., plastic, glass, metal, paper).
* Performs data augmentation and preprocessing to enhance the model's robustness.

### 3. Model Building with ResNet50
* Utilizes the pre-trained ResNet50 model architecture, fine-tuned on the garbage classification dataset.
* Configures the model with additional layers to adapt it to the specific classification task.

### 4. Model Training and Evaluation
* Trains the model using the processed dataset and monitors performance through accuracy and loss metrics.
* Evaluates the model's performance on a validation set to ensure generalization and avoid overfitting.

## API Deployment

### 1. FastAPI Creation
* We used FastAPI for creating the API.

### 2. Dockerization
* We dockerized the API.

### 3. API Deployment with Streamlit
* We run the API on Streamlit.

### Note: We dockerized the API just in case we used an alternate cloud service, but you can run the API directly on Streamlit!

## How to Use the API

### 1. Download the File
* Download file on your local device.

### 2. Open Folder Location
* Open the folder location, then write `cmd` on the navigation bar.

### 3. Run the Command
* Write this prompt in your terminal:
  ```bash
  streamlit run app.py
### 4. Upload Your Photo
* Use the provided interface to upload your photo for classification.
