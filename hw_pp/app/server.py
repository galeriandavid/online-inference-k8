from fastapi import FastAPI
from typing import List
import uvicorn

from hw_pp import PARAMS
from hw_pp.app.models import RequestBody, ResponseBody
from hw_pp.model import Model



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

def main():
    uvicorn.run("hw_pp.app.server:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()
