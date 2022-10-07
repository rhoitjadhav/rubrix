import os

PROJECT_NAME = "Rubrix API"

# ElasticSearch
ELASTIC_HOST = os.getenv("ELASTIC_HOST", "35.90.35.220")
ELASTIC_PORT = int(os.getenv("ELASTIC_PORT", "9200"))
ELASTIC_USER = os.getenv("ELASTIC_USER", "elastic")
ELASTIC_PASSWORD = os.getenv("ELASTIC_PASSWORD", "1234")

