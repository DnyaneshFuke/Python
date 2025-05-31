from fastapi import FastAPI, File, UploadFile, Request
import uvicorn
import numpy as np
from PIL import Image
from io import BytesIO
import tensorflow as tf
import os
from dotenv import load_dotenv
import cohere
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from starlette.responses import JSONResponse

load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
MODEL_PATH = os.getenv("MODEL_PATH")

co = cohere.Client(COHERE_API_KEY)

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

MODEL = tf.keras.models.load_model(MODEL_PATH)
class_names = ['Early_blight', 'Late_blight', 'Healthy']

def get_cure_and_prevention(disease: str) -> str:
    try:
        prompt = f"""
        You are an expert plant disease advisor. A farmer has detected {disease} in their potato crop.
        Provide the following in this Markdown format:
        **Symptoms**
        - symptom 1
        - symptom 2

        **Cures**
        - cure 1
        - cure 2

        **Prevention**
        - method 1
        - method 2
        """

        response = co.generate(
            model='command',
            prompt=prompt,
            max_tokens=300,
            temperature=0.7
        )

        if response.generations:
            return response.generations[0].text.strip()
        else:
            return "No information found."
    except Exception as e:
        return f"Error querying Cohere API: {str(e)}"

def read_imagefile(data):
    try:
        image = np.array(Image.open(BytesIO(data)))
    except Exception as e:
        raise ValueError(f"Image processing error: {str(e)}")
    return image

@app.get("/")
async def read_root():
    return {"message": "FastAPI is running. Use /uploadfile/ for file uploads."}

@app.post("/uploadfile/")
@limiter.limit("60/minute")
async def create_upload_file(request: Request, file: UploadFile = File(...)):
    try:
        image = read_imagefile(await file.read())
        image_batch = np.expand_dims(image, 0)

        prediction = MODEL.predict(image_batch)
        predicted_class = class_names[np.argmax(prediction[0])]
        prediction_probs = np.max(prediction[0])

        cure_and_prevention = get_cure_and_prevention(predicted_class)

        return {
            "Class": predicted_class,
            "Probability": float(prediction_probs),
            "Cure_and_Prevention": cure_and_prevention
        }
    except Exception as e:
        return {"error": str(e)}

@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"error": "Rate limit exceeded: Only 60 requests per minute. Try again later."}
    )

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
