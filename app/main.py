# The standard implementation of an FastAPI app
# Uvicorn will be used to serve the app

from fastapi import FastAPI
from app import __version__
from app.predict import prediction
from pydantic import BaseModel
import pandas as pd
from fastapi.encoders import jsonable_encoder

app = FastAPI()

class DataIn(BaseModel):
    OverallQual: int
    GrLivArea: int
    
class Result(BaseModel):
    result: float

@app.get("/")
async def root():
    return {"health check": "OK", "model_version": __version__}

@app.post("/predict")
def predict(house: DataIn):
    print(pd.DataFrame(dict(house), index=[0]))
    data = pd.DataFrame(dict(house), index=[0])
    result = prediction(data)
    return{"House price:": result}
  
    