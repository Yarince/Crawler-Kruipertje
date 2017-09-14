from elasticsearch import Elasticsearch
from properties import ElasticsearchProperties


class ElasticsearchConnection(object):
    """
    This class handles the connection with a Elasticsearch server
    """

    @staticmethod
    def get_connection():
        """
        This method will return a Elasticsearch connection
        :return: A elasticsearch connection
        """
        es = Elasticsearch([{'host': ElasticsearchProperties.HOST, 'port': ElasticsearchProperties.PORT}])
        if es.ping():
            return es
        else:
            raise ValueError("Connection failed")
