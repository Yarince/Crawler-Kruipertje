import unittest

from elasticsearch import Elasticsearch

from properties import ElasticsearchProperties
from persistence import ElasticsearchConnection


class ElasticsearchConnectionTest(unittest.TestCase):

    def setUp(self):
        self.sut = ElasticsearchConnection()
        self.old_host = ElasticsearchProperties.HOST

    def tearDown(self):
        ElasticsearchProperties.HOST = self.old_host

    def test_elasticsearch_instance(self):
        expected = Elasticsearch([{'host': ElasticsearchProperties.HOST, 'port': ElasticsearchProperties.PORT}])
        result = self.sut.get_connection()
        self.assertIsInstance(expected, result.__class__)

    def test_no_elasticsearch_instance(self):
        ElasticsearchProperties.HOST = '0.0.0.0'
        with self.assertRaises(ValueError):
            self.sut.get_connection()
