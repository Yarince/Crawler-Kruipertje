import unittest

from crawler import BlacklistService
from properties import Properties


class BlacklistServiceTest(unittest.TestCase):

    def setUp(self):
        self.sut = BlacklistService()
        Properties.BLACKLIST_FILE = '../test/test_crawler/test_blacklist_csv.csv'

    def test_in_blacklist(self):
        url_match = 'http://www.twitter.nl'
        url_no_match = 'http://technovium.nl'
        self.assertTrue(self.sut.in_blacklist(url_match))
        self.assertFalse(self.sut.in_blacklist(url_no_match))


