from fastapi import FastAPI, File, UploadFile, Request
import uvicorn
import numpy as np
from PIL import Image
from io import BytesIO
import tensorflow as tf
import os
from dotenv import load_dotenv
import google.generativeai as genai
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from starlette.responses import JSONResponse

# Load environment variables
load_dotenv()

# Access the Gemini API key from the .env file
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Model path
MODEL_PATH = os.getenv("MODEL_PATH")

# Initialize FastAPI and Rate Limiter (60 requests per minute)
limiter = Limiter(key_func=get_remote_address)
app = FastAPI()

# Add rate limiting error handling
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Load the model from the correct path
MODEL = tf.keras.models.load_model(MODEL_PATH)

# Class names corresponding to the model's output labels
class_names = ['Early_blight',  'Late_blight','Healthy']
def get_cure_and_prevention(disease: str) -> str:
    """
    Query Gemini API for cure and prevention of the given disease.
    Args:
        disease: Predicted disease class.
    Returns:
        A string containing cure and prevention details.
    """
    try:
        # Custom prompt for Gemini API
        prompt = f"""
        You are an expert plant disease advisor. A farmer has detected {disease} in their potato crop.
        Provide the following information:
        - Symptoms of {disease}
        - Immediate cures
        - Prevention methods
        Keep the explanation simple, concise, and actionable.
        """
        # Use Gemini API to generate a response
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        
        # Check if a response was returned
        if response.text:
            return response.text
        else:
            return "No information found."
    except Exception as e:
        return f"Error querying Gemini API: {str(e)}"
def read_imagefile(data) -> dict:
    """
    Preprocess the image and predict the class.
    Args:
        data: Image data in byte format.
    Returns:
        A dictionary containing the prediction and the associated probabilities.
    """
    try:
        # Open and preprocess the image (resize to 256x256 and normalize)
        image = np.array(Image.open(BytesIO(data))) #convert("RGB").resize((256, 256)))
        #image = image / 255.0  # Normalize to [0, 1]
         # Raw probabilities for all classes
        
        
    except Exception as e:
        raise ValueError(f"Error during image processing: {str(e)}")
    return image

@app.get("/")
async def read_root():
    """
    Root endpoint to check if the FastAPI app is running.
    """
    return {"message": "FastAPI is running. Use /uploadfile/ for file uploads."}

@app.post("/uploadfile/")
@limiter.limit("60/minute")  # Rate limiting: 60 requests per minute
async def create_upload_file(request: Request, file: UploadFile = File(...)):
    """
    Endpoint to handle file uploads, make predictions, and return results.
    """
    try:
        # Get the image data and process it
        image = read_imagefile(await file.read())
        image_batch = np.expand_dims(image, 0)  # Add batch dimension
        
        # Predict the class probabilities
        prediction = MODEL.predict(image_batch)
        predicted_class = class_names[np.argmax(prediction[0])]  # Class label
        prediction_probs = np.max(prediction[0]) 
        
        # Fetch cure and prevention details from Gemini API
        cure_and_prevention = get_cure_and_prevention(predicted_class)

        return {
            "Class": predicted_class,
            "Probability": float(prediction_probs),
            "Cure_and_Prevention": cure_and_prevention
        }
    except Exception as e:
        # Return error message if something goes wrong
        return {"error": str(e)}

@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    """
    Custom handler for rate limit exceeded.
    """
    return JSONResponse(
        status_code=429,
        content={"error": "Rate limit exceeded: Only 60 requests allowed per minute. Please try again later."}
    )

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)