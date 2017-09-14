from enums import HTML
from persistence.html_service import RedisService


class HTMLServiceFactory(object):
    """
    A Factory for handling the HTMLService instance
    """
    _instance = None
    _item = None

    def __init__(self, item):
        self._item = item

    def __new__(cls, *args, **kwargs):
        if HTMLServiceFactory._instance is None:
            HTMLServiceFactory._instance = super(HTMLServiceFactory, cls).__new__(cls)
        return HTMLServiceFactory._instance

    def get_instance(self):
        """
        Returns a HTML service instance
        :return: HTML service
        """
        if self._item == HTML.REDIS:
            return RedisService()
        else:
            raise TypeError("Instance {} is not known!".format(self._item))
