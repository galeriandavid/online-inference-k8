from joblib import dump
import json
import logging
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report

def train_model(data_path):
    logging.info("Prepare data")
    df = pd.read_csv(data_path)
    X, y = df.drop(columns="target"), df["target"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    logging.info("Grid search")
    param_grid = {
        "n_estimators": [25, 50, 75, 100],
        "max_depth": [1,2,3,4,5],  
    }
    grid_search = GridSearchCV(
        RandomForestClassifier(random_state=42),
        param_grid=param_grid,
        scoring="f1_macro"
        )
    grid_search.fit(X_train, y_train)
    clf = grid_search.best_estimator_

    logging.info("Test model")
    y_pred = clf.predict(X_test)
    report = classification_report(y_test, y_pred, output_dict=True)

    logging.info("Save model and metrics")
    dump(clf, "model/model_file/model.joblib")
    with open("model/model_file/metrics.json", "w", encoding="utf-8") as f:
        json.dump(report["weighted avg"] ,f)

if __name__ == "__main__":
    train_model("data/iris.csv")
