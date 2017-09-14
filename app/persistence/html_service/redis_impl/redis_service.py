from persistence import RedisConnection
from persistence.html_service import HTMLService


class RedisService(HTMLService):
    """
    This class can be used to communicate with the Redis server.
    """

    def __init__(self):
        self.connection = RedisConnection().get_connection()

    def get_html(self, key):
        """
        Returns the value of a given key from Redis
        :param key:
        :return: String
        """
        return self.connection.get(key)

    def save_html(self, key, value):
        """
        Saves a new key-value pair in Redis
        :param key:
        :param value:
        :return: nothing
        """
        self.connection.set(key, value)

    def set_list_value(self, list_name, value, expire=None):
        """
        Adds a value to the given list in Redis, the list will be created if it doesn't exist
        :param list_name:
        :param value:
        :param expire:
        :return: nothing
        """
        self.connection.rpush(list_name, value)
        if expire is not None:
            self.set_expire(list_name, expire)

    def get_list(self, list_name, begin=0, end=-1):
        """
        Returns (part of) a list from Redis.
        :param list_name:
        :param begin:
        :param end:
        :return: List
        """
        return self.connection.lrange(list_name, begin, end)

    def set_expire(self, key, time):
        self.connection.expire(key, time)
