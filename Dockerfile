FROM python:3.8.10

EXPOSE 8000

ENV ELASTIC_HOST "localhost"
ENV ELASTIC_PORT 9200
ENV ELASTIC_USER "elastic"
ENV ELASTIC_PASSWORD "changeme"

COPY ./requirements.txt /rubrix-challenge/
COPY ./src/ /rubrix-challenge/src

RUN pip install -r /rubrix-challenge/requirements.txt

WORKDIR /rubrix-challenge/src

CMD ["python", "main.py"]
