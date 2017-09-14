from persistence.datasource import ElasticsearchConnection
from persistence.parser_service import ParserService
from properties import Properties
from utils import JsonHelper


class ElasticsearchService(ParserService):

    def __init__(self):
        self.connection = ElasticsearchConnection().get_connection()

    def update_item(self, id, json, *args, **kwargs):
        """
        This method will update the json string so it works with Elasticsearch
        It will then update it to elasticsearch
        :param id: The id of the item
        :param json: json string
        :param args: *args
        :param kwargs: **kwargs
        :return: Nothing
        """
        result = {"doc": JsonHelper.to_dict(json), "doc_as_upsert": "true"}
        json_result = JsonHelper.to_json(result)
        self.connection.update(index=Properties.Elasticsearch.PARSER_INDEX,
                               doc_type=Properties.Elasticsearch.PARSER_DOC_TYPE,
                               id=id,
                               body=json_result,
                               *args,
                               **kwargs)
