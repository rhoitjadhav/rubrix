# Packages
from fastapi import Request
from fastapi.routing import APIRouter

# Modules
from utils.data_classes import ReturnValue
from apis.models.dataset_model import DATASET_INDEX
from apis.usecases.metrics_usecase import MetricsUsecase
from utils.elastic_search_interface import ElasticSearchInterface
from config import (
    ELASTIC_HOST,
    ELASTIC_PORT,
    ELASTIC_USER,
    ELASTIC_PASSWORD
)

hosts = [
    f"http://{ELASTIC_USER}:{ELASTIC_PASSWORD}@{ELASTIC_HOST}:{ELASTIC_PORT}/"
]
esh = ElasticSearchInterface(hosts)
dataset_usecase = MetricsUsecase(esh, DATASET_INDEX)
router = APIRouter(prefix="/metrics")


@router.post("/token-length-distribution")
async def token_length_distrubution(request: Request):
    try:
        payload = await request.json()
        return dataset_usecase.token_length_distribution(payload["dataset_ids"])

    except Exception as err:
        return ReturnValue(False,
                           "Error performing text length distribution",
                           error=repr(err))


@router.post("/token-frequencies")
async def token_frequencies(request: Request):
    try:
        payload = await request.json()
        return dataset_usecase.token_frequencies(payload["dataset_ids"])

    except Exception as err:
        return ReturnValue(False,
                           "Error calculating token frequencies",
                           error=repr(err))
