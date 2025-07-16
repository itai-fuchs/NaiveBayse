import uvicorn
from fastapi import FastAPI
from Clean_Table import Cleaner
from bayesian_model import BayesianModel
from classifier import BayesianClassifier


path = "C:/Users/itai/Downloads/archive (1)/FlavorSense.csv"
ct = Cleaner(path)

model = BayesianModel(ct.table)
app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "hello world"}

@app.get("/{name}")
async def root(name):
    name = name.split(".")
    s_dic = {}
    for i in range(0, len(name) ,2):
        s_dic[name[i]] = name[i+1]
    return {"answer": BayesianClassifier.prediction(s_dic, model.model, model.ratio_target_variable)}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)