import redis
from properties import RedisProperties


class RedisConnection(object):
    """
    This class handles the connection with a Redis server
    """
    @staticmethod
    def get_connection():
        """
        This method will return a redis connection
        :return: A Redis connection
        """
        return redis.StrictRedis(RedisProperties.HOST,
                                 RedisProperties.PORT,
                                 RedisProperties.DB,
                                 RedisProperties.PASSWORD)
