import logging
from APP.loader import Loader
from APP.cleaner import Cleaner
from naiveBayesTrainer import NaiveBayesTrainer
from APP.classifier import BayesianClassifier
from fastapi import FastAPI
import uvicorn
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("C:/Users/itai/PycharmProjects/Navie_Bayse/LOGS/app.log"),
        logging.StreamHandler()
    ]
)
path = "C:/Users/itai/PycharmProjects/Navie_Bayse/DATA/FlavorSense.csv"
logging.info(f"Loading data from {path}")  # Log start of data loading
load = Loader(path)
table = Cleaner(load.table).table
logging.info(f"Data loaded and cleaned: {table.shape[0]} rows, {table.shape[1]} columns")  # Log data shape after cleaning

logging.info("Training Naive Bayes model")  # Log start of model training
model = NaiveBayesTrainer(table)
logging.info("Model training complete")  # Log model training complete

app = FastAPI()

@app.get("/")
async def root():
    logging.info("Root endpoint called")  # Log root endpoint access
    return {"wellcom to the baysian model"}

@app.get("/{predict}")
async def predict_input(predict: str):
    logging.info(f"Prediction request received: {predict}")  # Log incoming prediction request
    predict = predict.split(".")
    s_dic = {}
    for i in range(0, len(predict), 2):
        s_dic[predict[i]] = predict[i + 1]
    answer = BayesianClassifier.prediction(s_dic, model.model, model.ratio_target_variable)
    logging.info(f"Prediction answer: {answer}")  # Log prediction result
    return {"answer": answer}

if __name__ == "__main__":
    logging.info("Starting server uvicorn on 127.0.0.1:8000")  # Log server startup
    uvicorn.run(app, host="127.0.0.1", port=8000)
