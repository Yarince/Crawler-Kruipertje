import unittest

from app.my_parser import Parser
from test.mock import MockRedis, MockElastic


class ParserTest(unittest.TestCase):

    def setUp(self):
        self.sut = Parser(MockRedis(), MockElastic())

    def test_add_link_to_que(self):
        expected = self.sut.queue.qsize() + 1
        self.sut.add_link_to_queue('link')
        self.assertEqual(expected, self.sut.queue.qsize())
