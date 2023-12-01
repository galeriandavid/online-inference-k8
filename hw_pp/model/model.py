from joblib import load
import pandas as pd
import hw_pp


class Model:
    def __init__(self):
        self.clf = load(hw_pp.__path__[0]+"/model/model_file/model.joblib")

    async def predict(self, X):
        X = pd.DataFrame([sample.dict() for sample in X])
        preds = self.clf.predict(X)
        probs = self.clf.predict_proba(X).max(axis=1)
        result = [
            {"pred": pred, "prob": prob} for pred, prob in zip(preds, probs)
        ]
        return {"predictions": result}