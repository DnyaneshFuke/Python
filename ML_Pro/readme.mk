Here is the complete README file in markdown format:

```markdown
# Potato Disease Classification App

This project involves creating a machine learning model to classify potato leaves as early blight, late blight, or healthy.
The model is integrated with an API that provides methods for curing diseases and recommending preventive measures. 
The application is deployed using **FastAPI** on a local server and exposed to a front-end Android app via **ngrok**.

## Project Structure

```
.
├── ML_Pro/
│   ├── Fast_api_server.py                 	   # FastAPI backend
│   ├── Model_tranning_script.ipynb            # Potato leaf classification model
│   ├── model/	                               # Contain pre-trained models
│   └── requirements.txt                       # List of dependencies
├── Frontend_app/                              # Front-end Android app 
├── data/                                      # Dataset downloaded from Kaggle https://www.kaggle.com/datasets/arjuntejaswi/plant-village/data
├── README.md                                  # Project documentation
└── environment.yml                            # Conda environment configuration
```

## Requirements

- **Python 3.9** (or higher)
- **FastAPI** for the backend
- **TensorFlow** (with GPU support)
- **ngrok** for exposing the local server to the front-end app thoruogh the internet
- **Flask** (for optional testing or additional features)
- **CUDA** for GPU support
- **Pillow** for image handling

### Backend Dependencies

You can install the necessary dependencies by running:

```bash
pip install -r requirements.txt
```

### Frontend Dependencies

The Android app is built using **Flutter**. Follow the instructions below to set up the front-end project.

## Setup Instructions

### Backend Setup

1. **Create a Conda Environment:**

   Use the provided `environment.yml` file to create the environment with all the necessary dependencies:

   ```bash
   conda env create -f environment.yml
   ```

2. **Activate the Conda Environment:**

   ```bash
   conda activate potato-disease-classification
   ```

3. **Run the FastAPI Backend:**

   Navigate to the `app/`  directory and run the Fast_api_server file to start the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

   This will start the server at `http://localhost:"yourport_no"`. If you are exposing the server to the internet, use **ngrok** to tunnel the server:

   ```bash
   ngrok http "yourport_no"
   ```

   The ngrok URL will be displayed in the terminal, and you can use it in your Android app to connect to the backend.

Important: test the backend by sending a POST request to the server with a potato leaf image. The backend will classify the image and return the prediction (early blight, late blight, or healthy) along with relevant disease prevention information.
4. **Testing the Backend:**

   You can test the backend by sending a POST request to the server with a potato leaf image. The backend will classify the image and return the prediction (early blight, late blight, or healthy) along with relevant disease prevention information.

### Frontend Setup (Android App)

1. **Set up Flutter:**

   Ensure that **Flutter** is installed on your machine. If you haven't already, follow the [Flutter installation guide](https://flutter.dev/docs/get-started/install) for your platform.

2. **Clone the Frontend_app repository:**

   Clone the repository for the Android app .
   Run main.dart file to start the app.
   and repace the url in the main.dart file with your ngrok url.

   ```bash
   git clone <android-app-repository-url>
   ```

3. **Update API URL in the Android App:**

   Open the Android app in your preferred IDE (e.g., Android Studio). Update the backend API URL to point to your **ngrok** URL or the local server (if running locally).

4. **Run the Android App:**

   Build and run the app on an emulator or connected device. The app will allow users to take a photo of a potato leaf and send it to the backend for classification.



### Model Training

If you want to train the model on your own dataset:

1. Prepare a dataset of potato leaf images with labels for each disease type (early blight, late blight, or healthy).
2. Use the `model.py` script to train the model using **TensorFlow**. The trained model can then be saved and loaded for use in the backend.

```python
# Example in model.py
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Train your model here
```

## Usage

1. **Start the FastAPI server** by running:

   ```bash
   uvicorn main:app --reload
   ```

2. **Run ngrok** to expose the backend if needed:

   ```bash
   ngrok http 8000
   ```

3. **Open the Android app** and take a photo of a potato leaf.
4. **Submit the image** to the backend API to get a classification result and disease prevention recommendations.

## Contributions

Contributions are welcome! Feel free to fork the repository, open issues, and submit pull requests.

NOTE:Train the model using the Model_tranning_script.ipynb provided, as the trained model file is not included in the repository.
     downloaded dataset from Kaggle https://www.kaggle.com/datasets/arjuntejaswi/plant-village/data