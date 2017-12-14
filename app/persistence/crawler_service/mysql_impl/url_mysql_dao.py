import pymysql

from datetime import timedelta, datetime
from socket import gethostbyname, gaierror
from domain import Url
from persistence.crawler_service.url_dao import UrlDAO
from utils import DomainParser, HashService
from persistence.datasource.mysql_impl import MySQLConnection


class UrlMySQLDAO(UrlDAO):
    """
    A class that will connect with the mysql database table URL
    """

    def get_url(self, url):
        """
        This method will return a specific url.
        :param url: the url
        :return: List with one record
        """
        query = "SELECT HEX(id) FROM url WHERE id = UNHEX('{0}')".format(str(HashService.md5(url)))
        conn = MySQLConnection().get_connection()
        cursor = conn.cursor()
        result = []
        try:
            # Escapes url string
            # Inserts escaped string in query and executes
            cursor.execute(query)
            result.append(cursor.fetchone())
        except pymysql.Error as e:
            code, msg = e.args
            print("MySQL Error [{0}]: {1}".format(str(code), msg))
        finally:
            if conn:
                cursor.close()
                conn.close()
        return result

    def get_queue_urls(self):
        """
        This method will return all url's that haven't been visited in the last x days from the database
        :return: all url's
        """
        conn = MySQLConnection().get_connection()
        cursor = conn.cursor()
        result = []
        try:
            date_today = str(datetime.today() - timedelta(days=0))
            query = "SELECT url FROM url WHERE last_visited <= '{0}' ORDER BY last_visited DESC"
            cursor.execute(query.format(date_today))
            for item in cursor.fetchall():
                url = item[0]
                x = Url(url)
                result.append(x)
        except pymysql.Error as e:
            code, msg = e.args
            print("MySQL Error [{0}]: {1}".format(str(code), msg))
        finally:
            if conn:
                cursor.close()
                conn.close()
        return result

    def get_urls(self):
        """
        This method will return all url's
        :return: all url's in a set
        """
        conn = MySQLConnection().get_connection()
        cursor = conn.cursor()
        result = set()
        try:
            query = "SELECT HEX(id) FROM url"
            cursor.execute(query)
            for item in cursor.fetchall():
                result.add(item[0])
        except pymysql.Error as e:
            code, msg = e.args
            print("MySQL Error [{0}]: {1}".format(str(code), msg))
        finally:
            if conn:
                cursor.close()
                conn.close()
        return result

    def add_queue_url(self, url, shortened_url):
        """
        This method will add a url to the database
        :param url: a url
        :param shortened_url: a shortened url
        :return: nothing
        """
        conn = MySQLConnection().get_connection()
        cursor = conn.cursor()
        try:
            host = gethostbyname(DomainParser.get_domain_name(url))
        except gaierror:
            host = '0.0.0.0'
        query = "INSERT INTO url (id, url, ip_address, last_visited, date_found) " \
                "VALUES (UNHEX('{0}'),{1},'{2}', '{3}', '{4}') " \
                "ON DUPLICATE KEY UPDATE ip_address = '{2}', last_visited = '{3}'"
        try:
            # Escapes url string
            text_url = conn.escape(str(url))
            # Inserts escaped string in query and executes
            cursor.execute(query.format(str(HashService.md5(shortened_url)),
                                        text_url,
                                        host,
                                        datetime.today(),
                                        datetime.today()))
            conn.commit()
        except pymysql.Error as e:
            code, msg = e.args
            print("MySQL Error [{0}]: {1}".format(str(code), msg))
            conn.rollback()
        finally:
            if conn:
                cursor.close()
                conn.close()
