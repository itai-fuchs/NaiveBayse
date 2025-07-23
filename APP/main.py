import logging
from loader import Loader
from cleaner import Cleaner
from naiveBayesTrainer import NaiveBayesTrainer
from classifier import BayesianClassifier
from testing import Testing
from fastapi import FastAPI
import uvicorn


def setup_logging():
    # Log all INFO and above messages to a file
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("C:/Users/itai/PycharmProjects/Navie_Bayse/LOGS/app.log"),
        ]
    )

    # Show only WARNING and above messages in the terminal
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
    logging.getLogger().addHandler(console_handler)


def load_data(path):
    # Load raw data from CSV using Loader class
    logging.info(f"Loading data from {path}")
    load = Loader(path)
    return load


def clean_data(load):
    # Clean the loaded data using Cleaner class
    table = Cleaner(load.table).table
    logging.info(f"Data loaded and cleaned: {table.shape[0]} rows, {table.shape[1]} columns")
    return table


def train_model(table):
    # Train Naive Bayes model using the cleaned data
    logging.info("Training Naive Bayes model")
    model = NaiveBayesTrainer(table)
    logging.info("Model training complete")
    test = Testing(table).result
    if not test:
        logging.warning("Model accuracy is too low. Server will not start.")
        exit(1)
    return model


def setup_routes(app, model):
    # Root endpoint
    @app.get("/")
    async def root():
        logging.info("Root endpoint called")
        return {"wellcom to the baysian model"}

    # Prediction endpoint
    @app.get("/{predict}")
    async def predict_input(predict: str):
        logging.info(f"Prediction request received: {predict}")
        predict = predict.split(".")  # Split input like: "feature1.value1.feature2.value2"
        s_dic = {}
        for i in range(0, len(predict), 2):
            s_dic[predict[i]] = predict[i + 1]
        # Use the model to predict
        answer = BayesianClassifier.prediction(s_dic, model.model, model.ratio_target_variable)
        logging.info(f"Prediction answer: {answer}")
        return {"answer": answer}




setup_logging()  # Configure logging

# Load and prepare data
path = "C:/Users/itai/PycharmProjects/Navie_Bayse/DATA/FlavorSense.csv"
load = load_data(path)
table = clean_data(load)

# Train model
model = train_model(table)


# Set up FastAPI application
app = FastAPI()
setup_routes(app, model)

if __name__ == "__main__":

    # Start the server
    logging.info("Starting server uvicorn on 127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)
