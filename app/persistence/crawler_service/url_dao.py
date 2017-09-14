from abc import ABCMeta, abstractmethod


class UrlDAO(metaclass=ABCMeta):
    """
    Base class for all UrlDAO classes
    """

    @abstractmethod
    def get_url(self, url):
        pass

    @abstractmethod
    def get_queue_urls(self):
        pass

    @abstractmethod
    def add_queue_url(self, url, shortened_url):
        pass
