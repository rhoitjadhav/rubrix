# Packages
from pydantic import BaseModel

DATASET_INDEX = "dataset"


class DatasetModel(BaseModel):
    text: str
