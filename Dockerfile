FROM python:3.9.13-slim

WORKDIR /online-inference-k8

COPY . /online-inference-k8

RUN pip install -r requirements.txt

CMD uvicorn src.app.server:app --port=8000 --host=0.0.0.0