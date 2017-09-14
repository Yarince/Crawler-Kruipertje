from enums import PARSER
from persistence.parser_service.elasticsearch_impl import ElasticsearchService


class ParserServiceFactory(object):
    """
    A Factory for handling the ParserServicee instance
    """
    _instance = None
    _item = None

    def __init__(self, item):
        self._item = item

    def __new__(cls, *args, **kwargs):
        if ParserServiceFactory._instance is None:
            ParserServiceFactory._instance = super(ParserServiceFactory, cls).__new__(cls)
        return ParserServiceFactory._instance

    def get_instance(self):
        """
        Returns a Parser service instance
        :return: Parser service
        """
        if self._item == PARSER.ELASTICSEARCH:
            return ElasticsearchService()
        else:
            raise TypeError("Instance {} is not known!".format(self._item))
