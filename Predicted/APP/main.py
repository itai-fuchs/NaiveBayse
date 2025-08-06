import os
import logging
import requests
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from APP.classifier import BayesianClassifier

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LOG_DIR = os.path.join(BASE_DIR, "LOGS")
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "predictor.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

app = FastAPI()

def get_model(url="http://model:8000/training"):
    logging.info(f"Fetching model from remote server at {url}")
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch model from remote server")
    data = response.json()
    if data.get("status") != "success":
        raise Exception(data.get("message", "Unknown error from server"))
    model = data.get("model")
    ratio_target_variable = data.get("ratio_target_variable")
    if model is None or ratio_target_variable is None:
        raise Exception("Invalid model data received")
    return model, ratio_target_variable

@app.get("/predict/{predict}")
async def predict_input(predict: str):
    try:
        parts = predict.split(".")
        s_dic = {parts[i]: parts[i+1] for i in range(0, len(parts), 2)}
        model_dict, target_ratio = get_model()
        answer = BayesianClassifier.prediction(s_dic, model_dict, target_ratio)
        return {"answer": answer}
    except Exception as e:
        logging.error(f"Prediction failed: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})
