FROM python:3.8.10

# Exposing port
EXPOSE 8000

# Environment Variables
ENV ELASTIC_HOST "localhost"
ENV ELASTIC_PORT 9200
ENV ELASTIC_USER "elastic"
ENV ELASTIC_PASSWORD "changeme"

# Copying source code
COPY ./requirements.txt /rubrix-challenge/
COPY ./src/ /rubrix-challenge/src

# Installing dependencies
RUN pip install -r /rubrix-challenge/requirements.txt

# Setting working directory
WORKDIR /rubrix-challenge/src

# Running application
CMD ["python", "main.py"]
