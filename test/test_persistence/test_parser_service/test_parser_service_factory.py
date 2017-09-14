import unittest
from enums import PARSER
from persistence import ParserServiceFactory, ElasticsearchService


class HtmlServiceFactoryTest(unittest.TestCase):

    def test_wrong_instance(self):
        self.sut = ParserServiceFactory('notredis')
        with self.assertRaises(TypeError):
            self.sut.get_instance()

    def test_es_instance(self):
        self.sut = ParserServiceFactory(PARSER.ELASTICSEARCH)
        expected = ElasticsearchService()
        result = self.sut.get_instance()
        self.assertIsInstance(expected, result.__class__)
