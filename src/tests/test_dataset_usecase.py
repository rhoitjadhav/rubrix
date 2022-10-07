# Packages
import unittest

# Modules
from apis.usecases.dataset_usecase import DatasetUsecase
from apis.models.dataset_model import DATASET_INDEX, DatasetModel
from utils.elastic_search_interface import ElasticSearchInterface
from config import (
    ELASTIC_USER,
    ELASTIC_HOST,
    ELASTIC_PORT,
    ELASTIC_PASSWORD
)

hosts = [
    f"http://{ELASTIC_USER}:{ELASTIC_PASSWORD}@{ELASTIC_HOST}:{ELASTIC_PORT}/"]

es_client = ElasticSearchInterface(hosts)


class TestDatasetUsecase(unittest.TestCase):
    _dataset_usecase = DatasetUsecase(es_client, DATASET_INDEX)

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

        self._dataset_usecase.add_dataset_by_text(dm1)
        self._dataset_usecase.add_dataset_by_text(dm2)

    def test_add_dataset_by_text(self):
        text = "In the United States the per capita costs of schooling " \
               "have risen almost as fast as the cost of medical " \
               "treatment. But increased treatment by both doctors and " \
               "teachers has shown steadily declining results. " \
               "Medical expenses concentrated on those above forty-five " \
               "have doubled several times over a period of forty years " \
               "with a resulting 3 percent increase in the life " \
               "expectancy of men. The increase in educational " \
               "expenditures has produced even stranger results; " \
               "otherwise President Nixon could not have been moved " \
               "this spring to promise that every child shall soon have " \
               "the “Right to Read” before leaving school."

        dm = DatasetModel(text=text)
        result = self._dataset_usecase.add_dataset_by_text(dm)
        self.assertTrue(result.success)

    def test_query_dataset(self):
        query = {
            "bool": {
                "filter": [
                    {
                        "query_string": {
                            "query": "school*"
                        }
                    }
                ]
            }
        }
        result = self._dataset_usecase.query_dataset(query)
        self.assertTrue(result.success)
