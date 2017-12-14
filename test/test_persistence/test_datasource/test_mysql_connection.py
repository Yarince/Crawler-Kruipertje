import unittest

import pymysql

from database_properties import DatabaseProperties
from persistence import MySQLConnection


class MySqlConnectionTest(unittest.TestCase):
    def setUp(self):
        self.sut = MySQLConnection()

    def test_mysql_instance(self):
        expected = pymysql.connect(DatabaseProperties.HOST,
                                   DatabaseProperties.USER,
                                   DatabaseProperties.PASSWORD,
                                   DatabaseProperties.DB)
        result = self.sut.get_connection()
        self.assertIsInstance(expected, result.__class__)

    def test_reopen_conn(self):
        self.sut.get_connection().close()
        expected = pymysql.connect(DatabaseProperties.HOST,
                                   DatabaseProperties.USER,
                                   DatabaseProperties.PASSWORD,
                                   DatabaseProperties.DB)

        result = self.sut.get_connection()
        self.assertIsInstance(expected, result.__class__)
