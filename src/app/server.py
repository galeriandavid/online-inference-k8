from fastapi import FastAPI
from typing import List

from src import PARAMS
from src.app.models import RequestBody, ResponseBody
from src.model import Model



app = FastAPI()
model = Model()


@app.post("/predict")
async def predict(samples: List[RequestBody]) -> ResponseBody:
    """Generate predictions

    Args:
        samples (List[RequestBody]): list of samples

    Returns:
        ResponseBody: Predictions
    """
    predictions = await model.predict(samples)
    return ResponseBody.parse_obj(predictions)
