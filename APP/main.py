import os
import logging
from APP.loader import Loader
from APP.cleaner import Cleaner
from APP.naiveBayesTrainer import NaiveBayesTrainer
from APP.classifier import BayesianClassifier
from fastapi import FastAPI
# import uvicorn

# Define the base directory (parent folder of APP)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Define the logs directory path and create it if it doesn't exist
LOG_DIR = os.path.join(BASE_DIR, "LOGS")
os.makedirs(LOG_DIR, exist_ok=True)

# Define the full log file path
LOG_FILE = os.path.join(LOG_DIR, "app.log")

# Configure logging to write to file and console
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

# Define the data directory path and file path for the CSV
DATA_DIR = os.path.join(BASE_DIR, "DATA")
path = os.path.join(DATA_DIR, "FlavorSense.csv")

# Log the path from which data will be loaded
logging.info(f"Loading data from {path}")

# Load data using Loader class
load = Loader(path)

# Clean the loaded data using Cleaner class
table = Cleaner(load.table).table
logging.info(f"Data loaded and cleaned: {table.shape[0]} rows, {table.shape[1]} columns")

# Log the start of model training
logging.info("Training Naive Bayes model")

# Train the Naive Bayes model on the cleaned data
model = NaiveBayesTrainer(table)
logging.info("Model training complete")

# Create FastAPI app instance
app = FastAPI()

# Define root endpoint returning a welcome message
@app.get("/")
async def root():
    logging.info("Root endpoint called")
    return {"wellcom to the baysian model"}

# Define prediction endpoint that receives input string and returns prediction result
@app.get("/{predict}")
async def predict_input(predict: str):
    logging.info(f"Prediction request received: {predict}")
    predict = predict.split(".")
    s_dic = {}
    for i in range(0, len(predict), 2):
        s_dic[predict[i]] = predict[i + 1]
    # Call the classifier to make a prediction based on input dictionary
    answer = BayesianClassifier.prediction(s_dic, model.model, model.ratio_target_variable)
    logging.info(f"Prediction answer: {answer}")
    return {"answer": answer}

