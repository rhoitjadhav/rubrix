# Packages
import unittest

# Modules
from apis.usecases.metrics_usecase import MetricsUsecase
from apis.usecases.dataset_usecase import DatasetUsecase
from utils.elastic_search_interface import ElasticSearchInterface
from apis.models.dataset_model import DATASET_INDEX, DatasetModel
from config import (
    ELASTIC_USER,
    ELASTIC_HOST,
    ELASTIC_PORT,
    ELASTIC_PASSWORD
)

hosts = [
    f"http://{ELASTIC_USER}:{ELASTIC_PASSWORD}@{ELASTIC_HOST}:{ELASTIC_PORT}/"]

es_client = ElasticSearchInterface(hosts)


class TestMetricstUsecase(unittest.TestCase):
    _dataset_usecase = DatasetUsecase(es_client, DATASET_INDEX)
    _metrics_dataset = MetricsUsecase(es_client, DATASET_INDEX)

    def setUp(self) -> None:
        text1 = "It may take a while to reach the ten percent level of cure, " \
                "because any newly established program will not have " \
                "cultivated the word-of-mouth advertising needed to " \
                "ensure its success"
        dm1 = DatasetModel(text=text1)
        text2 = "Obligatory schooling inevitably polarizes a society; " \
                "it also grades the nations of the world according " \
                "to an international"
        dm2 = DatasetModel(text=text2)

        result1 = self._dataset_usecase.add_dataset_by_text(dm1)
        self._id1 = result1.data["_id"]

        result2 = self._dataset_usecase.add_dataset_by_text(dm2)
        self._id2 = result2.data["_id"]

    def test_token_length_distribution(self):
        """
        Test token length distribution of datasets
        """
        dataset_ids = [
            {"_id": self._id1},
        ]

        result = self._metrics_dataset.token_length_distribution(dataset_ids)
        freq = result.data[0]["frequecies"][2]
        self.assertEqual(4, freq)

    def test_token_frequencies(self):
        """
        Test token frequecies of datasets
        """
        dataset_ids = [
            {"_id": self._id2},
        ]
        result = self._metrics_dataset.token_frequencies(dataset_ids)
        freq = result.data[0]["frequecies"]["the"]
        self.assertEqual(2, freq)
