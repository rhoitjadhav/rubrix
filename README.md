# Rubrix-Challlenge

## Requirements

- Python 3.8
- FastAPI
- Elasticsearch

## Running Application

First we need to create virtualenv along with installing python packages.
After successful, installation we will run the fastapi application.
Following are the commands which does the same.

```commandline
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
cd src
python main.py
```

Output:

```commandline
INFO:     Started server process [151577]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

Test Application by hitting the docs API

```commandline
curl http://localhost:8000/docs
```

## Running Tests

```commandline
cd src
python test.py
```

## Deployment

For deployment, we first need to build docker image. After successfully buildling image,
we can now simply run the docker image in a container.

Docker build and run commands:

```commandline
docker build -t test/test:1 -f Dockerfile .
docker run -d --name api -p 8000:8000 test/test:1
```

In k8s folder, there is `api-deployment.yaml` file which is used for deploying application on
kubernetes.
