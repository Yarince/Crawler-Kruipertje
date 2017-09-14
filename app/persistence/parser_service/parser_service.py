from abc import ABCMeta, abstractmethod


class ParserService(metaclass=ABCMeta):
    """
    Base class of the ParserService
    """
    @abstractmethod
    def update_item(self, *args, **kwargs):
        pass
