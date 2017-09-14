import pymysql
from database_properties import DatabaseProperties


class MySQLConnection:
    """
    This class handles the connection with a MySQL database
    """
    _instance = None

    @staticmethod
    def get_connection():
        """
        This method will return a MySQL connection
        :return: A MySQL connection
        """
        if MySQLConnection._instance is None:
            MySQLConnection._conn = pymysql.connect(DatabaseProperties.HOST,
                                                    DatabaseProperties.USER,
                                                    DatabaseProperties.PASSWORD,
                                                    DatabaseProperties.DB)
            MySQLConnection._instance = MySQLConnection._conn
        elif not MySQLConnection._conn.open:
            MySQLConnection._instance = pymysql.connect(DatabaseProperties.HOST,
                                                        DatabaseProperties.USER,
                                                        DatabaseProperties.PASSWORD,
                                                        DatabaseProperties.DB)
        return MySQLConnection._instance
