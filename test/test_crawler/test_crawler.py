import unittest

from crawler import Crawler
from enums import HTML, PARSER, DB
from my_parser import Parser
from properties import Properties
from test.mock.url_dao_mock import UrlDAOMock


class CrawlerTest(unittest.TestCase):
    def setUp(self):
        self.sut = Crawler(DB.MYSQL, HTML.REDIS, Parser(HTML.REDIS, PARSER.ELASTICSEARCH))

    def test_start(self):
        pass

    def test_create_workers(self):
        pass
