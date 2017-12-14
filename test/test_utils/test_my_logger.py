import os
import unittest

from enums import LOG
from properties import Properties
from utils import MyLogger


class MyLoggerTest(unittest.TestCase):

    def setUp(self):
        self.sut = MyLogger
        Properties.CRAWLER_LOG_FILE = "crawler.log"
        Properties.SPIDER_LOG_FILE = "spider.log"

    def test_spider_log(self):
        expected = "This is a test log\n"
        self.sut.log(LOG.SPIDER, "This is a test log")

        with open(Properties.SPIDER_LOG_FILE, "r") as file:
            actual = file.read()
            self.assertEqual(expected, actual[20:])

        os.remove(Properties.SPIDER_LOG_FILE)

    def test_crawler_log(self):
        expected = "This is a test log\n"
        self.sut.log(LOG.CRAWLER, "This is a test log")

        with open(Properties.CRAWLER_LOG_FILE, "r") as file:
            actual = file.read()
            self.assertEqual(expected, actual[20:])

        os.remove(Properties.CRAWLER_LOG_FILE)

