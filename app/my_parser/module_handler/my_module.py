from abc import ABCMeta, abstractmethod


class Module(metaclass=ABCMeta):
    """
    Base class for all my_modules
    """

    @property
    def run_all_pages(self):
        raise NotImplementedError

    def __init__(self):
        self.attributes = dict()

    @abstractmethod
    def handle_html_data(self, data):
        pass

    @abstractmethod
    def is_found(self):
        """
        Method to check if the current module has been found.
        :return: Boolean
        """
        if len(self.attributes) > 0:
            return True
        return False
