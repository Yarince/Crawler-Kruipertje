import unittest
import redis

from properties import RedisProperties
from persistence import RedisConnection


class RedisConnectionTest(unittest.TestCase):

    def setUp(self):
        self.sut = RedisConnection().get_connection()

    def test_redis_instance(self):
        expected = redis.StrictRedis(RedisProperties.HOST,
                                     RedisProperties.PORT,
                                     RedisProperties.DB,
                                     RedisProperties.PASSWORD)
        result = self.sut
        self.assertIsInstance(expected, result.__class__)
