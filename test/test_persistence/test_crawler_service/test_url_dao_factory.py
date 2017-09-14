import unittest

from enums import DB
from persistence import UrlDAOFactory, UrlMySQLDAO


class UrlDAOFactoryTest(unittest.TestCase):

    def test_wrong_instance(self):
        self.sut = UrlDAOFactory('mssql')
        with self.assertRaises(TypeError):
            self.sut.get_instance()

    def test_mysql_instance(self):
        self.sut = UrlDAOFactory(DB.MYSQL)
        expected = UrlMySQLDAO()
        result = self.sut.get_instance()
        self.assertIsInstance(expected, result.__class__)
