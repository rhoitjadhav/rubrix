# Packages
from typing import Dict

# Modules
from utils.data_classes import ReturnValue
from apis.models.dataset_model import DatasetModel
from utils.elastic_search_interface import ElasticSearchInterface


class DatasetUsecase:
    def __init__(self, elastic_search_client: ElasticSearchInterface,
                 dataset_index: str):
        self._es_client = elastic_search_client
        self._dataset_index = dataset_index

    def add_dataset_by_text(self, dataset: DatasetModel) -> ReturnValue:
        """
        Add dataset into elasticsearch by text as input

        Args:
            dataset: text based dataset

        Returns:
            Status of the operation
        """
        res = self._es_client.add(self._dataset_index, dataset.dict())
        return ReturnValue(True, "Dataset added successfully", data=dict(res))

    def add_dataset_by_file(self):
        pass

    def get_datasets(self, id_=None) -> ReturnValue:
        """
        Retrieves dataset by dataset id

        Args:
            id_: dataset id

        Returns:
            dataset if dataset exists otherwise empty data
        """
        query = {"match_all": {}}
        if id_:
            res = self._es_client.get(self._dataset_index, id_)
        else:
            res = self._es_client.search(self._dataset_index, query)

        return ReturnValue(True,
                           "Datasets successfully retrieved",
                           data=dict(res))

    def query_dataset(self, query: Dict) -> ReturnValue:
        """
        Query on dataset based on query parameters

        Args:
            query: elasticsearch query

        Returns:
            dataset if query parameter matches
        """
        res = self._es_client.search(self._dataset_index, query)
        return ReturnValue(True, "Data retrieved", data=dict(res))
