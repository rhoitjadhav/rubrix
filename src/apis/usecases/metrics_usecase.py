# Packages
import nltk
from typing import List, Dict
from collections import Counter

# Modules
from utils.data_classes import ReturnValue
from utils.elastic_search_interface import ElasticSearchInterface


class MetricsUsecase:
    def __init__(self, elastic_search_client: ElasticSearchInterface,
                 dataset_index: str):
        self._es_client = elastic_search_client
        self._dataset_index = dataset_index

    def _calculate_text_length_freq(self, text: str) -> Dict:
        """"""
        words = nltk.word_tokenize(text)
        text_lengths = [len(w) for w in words]

        return dict(Counter(text_lengths))

    def _calculate_token_frequecies(self, text: str) -> Dict:
        """"""
        words = nltk.word_tokenize(text)
        return dict(Counter(words))

    def token_length_distribution(
            self,
            dataset_ids: List
    ) -> ReturnValue:
        """
        Calculate token length distribution data
        Args:
            dataset_ids: list of dataset ids

        Returns:
            List of token length distribution data for requested datasets
        """
        result = self._es_client.mget(self._dataset_index, dataset_ids)

        distribution = []
        for res in result["docs"]:
            dataset_id = res["_id"]
            text = res["_source"]["text"]
            freq = self._calculate_text_length_freq(text)

            distribution.append({
                "dataset_id": dataset_id,
                "frequecies": freq
            })

        return ReturnValue(
            True,
            "Token length distribution data retrieved",
            data=distribution
        )

    def token_frequencies(self, dataset_ids: List):
        """
        Calculate token frequecies from the datasets

        Args:
            dataset_ids: list of dataset ids

        Returns:
            List of token frequencies for request datasets
        """
        result = self._es_client.mget(self._dataset_index, dataset_ids)

        distribution = []
        for res in result["docs"]:
            dataset_id = res["_id"]
            text = res["_source"]["text"]
            freq = self._calculate_token_frequecies(text)

            distribution.append({
                "dataset_id": dataset_id,
                "frequecies": freq
            })

        return ReturnValue(
            True,
            "Token frequecies data retrieved",
            data=distribution
        )
