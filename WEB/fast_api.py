import uvicorn
from fastapi import FastAPI


app=FastAPI()

@app.get("/")
async def root():
    return {"message":"hello looby"}

@app.get("/apertment1")
def add():
    return {"result":"mr david"}

@app.get("/apertment2")
def add():
    return {"result":"ms lea"}

@app.get("/{name}")
def name(name):
    return {"hello":name}

@app.get("/{age}")
def age(age):
    return {"hello":age}
if __name__=="__main__":

    uvicorn.run(app,host="127.0.0.1",port=8000)


