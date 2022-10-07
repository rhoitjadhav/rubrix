# Packages
import elasticsearch
from typing import List, Dict, Union
from elasticsearch import Elasticsearch
from elastic_transport import ObjectApiResponse


class ElasticSearchInterface:
    """
    This class is reponsible for interating with ElasticSearch API

    Args:
        hosts: list of elastic host
        timeout: timeout in seconds
        max_retries: maximum number of retries before an exception is propagated
        retry_on_timeout: should time out trigger a retry on different node
    """

    def __init__(
            self,
            hosts: List,
            timeout=3000,
            max_retries=10,
            retry_on_timeout=True
    ):
        self._elastic_client = Elasticsearch(
            hosts=hosts,
            timeout=timeout,
            max_retries=max_retries,
            retry_on_timeout=retry_on_timeout
        )

    def search(self, index: str, query: dict, size: int = 10,
               track_total_hits=True) -> ObjectApiResponse:
        """
        Searches on elastic search based on query
        Args:
            index: name of index
            size: numnber of documents to be returned
            query: query to elastic search
            track_total_hits: True if result should include total number of hits
                                matching the query otherwise False

        Returns:
            Result from qyerying elastic search
        """
        return self._elastic_client.search(index=index, query=query, size=size,
                                           track_total_hits=track_total_hits)

    def get(self, index: str, id_: str) -> Union[ObjectApiResponse, Dict]:
        """
        Get document by id
        Args:
            index: name of index
            id_: document id

        Returns:
            document or empty dict
        """
        try:
            return self._elastic_client.get(index=index, id=id_)

        except elasticsearch.NotFoundError:
            return {}

    def mget(self, index: str, docs: List):
        """
        Retrieves collection of documents based on multiple document ids

        Args:
            index: name of index
            docs: list of dataset ids

        Returns:
            Matched documents
        """
        return self._elastic_client.mget(index=index, docs=docs)

    def add(self, index, document) -> ObjectApiResponse:
        """
        Add document to elasticsearch

        Args:
            index: name of index
            document: json based document

        Returns:
            Acknowledged response from Elasticsearch server
        """
        return self._elastic_client.index(index=index, document=document)
