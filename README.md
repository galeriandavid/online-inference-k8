<div>
    <a href="https://github.com/galeriandavid/online-inference-k8/actions/workflows/test.yaml"><img src="https://github.com/galeriandavid/online-inference-k8/actions/workflows/test.yaml/badge.svg"></a>
    <a href="https://test.pypi.org/project/hw-pp/#files"><img src="https://github.com/galeriandavid/online-inference-k8/actions/workflows/pypi.yaml/badge.svg"></a>
</div>

## Online inference with FastAPI and kubernetes

Repository provides an example of running online inference with FastAPI and kubernetes

## Usage

1. Install docker and docker compose
2. Clone this repo

    ```bash
    git clone https://github.com/galeriandavid/online-inference-k8.git
    ```
3. Move to repo

    ```bash
    cd online-inference-k8
    ```
4. Build docker image

    ```bash
    docker build -t online-inference-k8 .
    ```

5. Create deployment

    ```bash
    kubectl create -f ./k8/deployment/deployment.yaml
    ```

6. Create service

    ```bash
    kubectl expose deployment online-inference-k8 --port 8000 --type=LoadBalancer --name iris-prediction-service
    ```

7. Try prediction service at http://127.0.0.1:8000/docs

8. Delete deployment and service

    ```bash
    kubectl delete deployment test-ml-score-api
    kubectl delete service test-ml-score-api-lb
    ```

## Install using pip

1. Install
    ```bash
    pip install -i https://test.pypi.org/simple/ hw-pp
    ```
2. Start
    ```bash
    iris
    ```