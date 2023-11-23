from joblib import load
import pandas as pd
import logging

from src import PARAMS
from src.app.models import ResponseBody

class Model:
    def __init__(self):
        self.clf = load(PARAMS["model_path"])

    async def predict(self, X):
        X = pd.DataFrame([sample.dict() for sample in X])
        preds = self.clf.predict(X)
        probs = self.clf.predict_proba(X).max(axis=1)
        result = [
            {"pred": pred, "prob": prob} for pred, prob in zip(preds, probs)
        ]
        return {"predictions": result}