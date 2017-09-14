from persistence.crawler_service.mysql_impl.url_mysql_dao import UrlMySQLDAO
from enums import DB


class UrlDAOFactory(object):
    """
    A factory class that will return a UrlDAO instance
    """
    _instance = None
    _item = None

    def __init__(self, item):
        self._item = item

    def __new__(cls, *args, **kwargs):
        if UrlDAOFactory._instance is None:
            UrlDAOFactory._instance = super(UrlDAOFactory, cls).__new__(cls)
        return UrlDAOFactory._instance

    def get_instance(self):
        """
        Returns a DAO instance
        :return: DAO instance
        """
        if self._item == DB.MYSQL:
            return UrlMySQLDAO()
        else:
            raise TypeError("Instance {} is not known!".format(self._item))
