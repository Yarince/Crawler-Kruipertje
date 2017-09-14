import unittest
from enums import HTML
from persistence import HTMLServiceFactory, RedisService


class HtmlServiceFactoryTest(unittest.TestCase):

    def test_wrong_instance(self):
        self.sut = HTMLServiceFactory('elasticsearch')
        with self.assertRaises(TypeError):
            self.sut.get_instance()

    def test_redis_instance(self):
        self.sut = HTMLServiceFactory(HTML.REDIS)
        expected = RedisService()
        result = self.sut.get_instance()
        self.assertIsInstance(expected, result.__class__)
