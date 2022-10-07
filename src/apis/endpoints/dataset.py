# Packages
from fastapi import Request
from fastapi.routing import APIRouter

# Modules
from utils.data_classes import ReturnValue
from apis.usecases.dataset_usecase import DatasetUsecase
from utils.elastic_search_interface import ElasticSearchInterface
from apis.models.dataset_model import DatasetModel, DATASET_INDEX
from config import (
    ELASTIC_HOST,
    ELASTIC_PORT,
    ELASTIC_USER,
    ELASTIC_PASSWORD
)

hosts = [
    f"http://{ELASTIC_USER}:{ELASTIC_PASSWORD}@{ELASTIC_HOST}:{ELASTIC_PORT}/"
]
es_client = ElasticSearchInterface(hosts)
dataset_usecase = DatasetUsecase(es_client, DATASET_INDEX)
router = APIRouter()


@router.post("/dataset")
def add_dataset(dataset: DatasetModel) -> ReturnValue:
    try:
        return dataset_usecase.add_dataset_by_text(dataset)
    except Exception as err:
        return ReturnValue(False, "Error while adding dataset", error=repr(err))


@router.get("/dataset")
def get_datasets() -> ReturnValue:
    try:
        return dataset_usecase.get_datasets()
    except Exception as err:
        return ReturnValue(False, "Error while retriving dataset",
                           error=repr(err))


@router.get("/dataset/{dataset_id}")
def get_dataset(dataset_id) -> ReturnValue:
    try:
        return dataset_usecase.get_datasets(id_=dataset_id)
    except Exception as err:
        return ReturnValue(False,
                           f"Error while retrieving dataset: {dataset_id}",
                           error=repr(err))


@router.post("/dataset-query")
async def query_dataset(request: Request):
    try:
        payload = await request.json()
        return dataset_usecase.query_dataset(payload["query"])
    except Exception as err:
        return ReturnValue(False,
                           "Error while querying dataset",
                           error=repr(err))
