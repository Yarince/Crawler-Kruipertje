from unittest import TestCase
from crawler import Spider
from domain import Url
from properties import Properties

from test.mock import MockRedis
from test.mock.url_dao_mock import UrlDAOMock


class SpiderTest(TestCase):
    def setUp(self):
        self.sut = Spider(Url('https://www.technovium.nl', 1), 'testSpider', UrlDAOMock(), MockRedis())
        Properties.SPIDER_MAX_PAGES = 1

    def tearDown(self):
        Properties.SPIDER_MAX_PAGES = 100
        Properties.SPIDER_MAX_DEPTH = 5

    def test_add_links_to_queue(self):
        Properties.SPIDER_MAX_DEPTH = 0
        self.sut.run()
        self.assertGreater(1, len(self.sut.deque))

    def test_http_error(self):
        Properties.SPIDER_MAX_DEPTH = 1
        self.sut = Spider(Url('http://example.com/', 1), 'testSpider', UrlDAOMock(), MockRedis())
        self.sut.run()
        self.assertGreater(len(self.sut.crawled), 0)





