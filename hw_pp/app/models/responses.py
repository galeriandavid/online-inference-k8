from pydantic import BaseModel
from typing import Dict, List

class Prediction(BaseModel):
    pred: str
    prob: float

class ResponseBody(BaseModel):
    predictions: List[Prediction]
