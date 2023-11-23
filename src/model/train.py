from joblib import dump
import json
import logging
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import f1_score, classification_report

from src import PARAMS

if __name__ == "__main__":
    logging.info("Prepare data")
    df = pd.read_csv(PARAMS["data_path"])
    X, y = df.drop(columns="target"), df["target"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=PARAMS["test_size"],
        random_state=PARAMS["SEED"],
        stratify=y
    )

    logging.info("Grid search")
    param_grid = {
        "n_estimators": [25, 50, 75, 100],
        "max_depth": [1,2,3,4,5],  
    }
    grid_search = GridSearchCV(
        RandomForestClassifier(random_state=PARAMS["SEED"]),
        param_grid=param_grid,
        scoring="f1_macro"
        )
    grid_search.fit(X_train, y_train)
    clf = grid_search.best_estimator_

    logging.info("Test model")
    y_pred = clf.predict(X_test)
    report = classification_report(y_test, y_pred, output_dict=True)

    logging.info("Save model and metrics")
    dump(clf, PARAMS["model_path"])
    with open(PARAMS["metrics_path"], "w", encoding="utf-8") as f:
        json.dump(report["weighted avg"] ,f)
