from abc import ABCMeta, abstractmethod


class HTMLService(metaclass=ABCMeta):
    """
    The base class for the HTMLService
    """

    @abstractmethod
    def save_html(self, key, value):
        pass

    @abstractmethod
    def get_html(self, key):
        pass
