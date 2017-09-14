import unittest

from properties import Properties
from crawler.blacklist_service import BlacklistService
from my_exceptions.blacklist_not_found_error import BlacklistNotFoundError


class CSVServiceTest(unittest.TestCase):

    def setUp(self):
        Properties.BLACKLIST_FILE = '../test/test_crawler/test_blacklist_csv.csv'
        self.sut = BlacklistService()
        self.test_site = 'http://technovium.nl'
        self.site_in_blacklist = 'http://www.twitter.com'

    def tearDown(self):
        Properties.BLACKLIST_FILE = 'blacklist.csv'

    def test_in_blacklist(self):
        self.assertTrue(self.sut.in_blacklist(self.site_in_blacklist))

    def test_not_in_blacklist(self):
        self.assertFalse(self.sut.in_blacklist(self.test_site))

    def test_open_empty_file(self):
        Properties.BLACKLIST_FILE = 'Empty'
        with self.assertRaises(BlacklistNotFoundError):
            self.sut.in_blacklist(self.test_site)
