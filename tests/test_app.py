import pytest
from fastapi.testclient import TestClient


from hw_pp.app.server import app
from hw_pp.app.models import RequestBody


client = TestClient(app)

test_query = [
    {
        "sepal_length_cm": 1,
        "sepal_width_cm": 2,
        "petal_length_cm": 3.4,
        "petal_width_cm": -1
    }
]

def test_predict_many():
    """test response status"""
    response = client.post("/predict", json=test_query)
    assert response.status_code == 200
