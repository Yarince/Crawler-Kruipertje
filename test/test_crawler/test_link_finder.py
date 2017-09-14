import unittest

from crawler import LinkFinder
from domain import Url
from my_exceptions import BlacklistNotFoundError
from properties import Properties


class LinkFinderTest(unittest.TestCase):
    def setUp(self):
        Properties.BLACKLIST_FILE = '../test/test_crawler/test_blacklist_csv.csv'
        self.base_url = Url('http://www.technovium.nl')
        self.page_url = Url('http://www.technovium.nl')
        self.sut = LinkFinder(page_url=self.page_url)

    def test_url_with_http(self):
        self.sut.handle_starttag('a', [('href', 'http://www.technovium.nl')])
        actual = str(self.sut.links.pop())
        expected = 'http://www.technovium.nl'
        self.assertEqual(actual, expected)

    def test_url_with_https(self):
        self.sut.handle_starttag('a', [('href', 'https://www.technovium.nl')])
        actual = str(self.sut.links.pop())
        expected = 'https://www.technovium.nl'
        self.assertEqual(actual, expected)

    def test_url_with_www(self):
        self.sut.handle_starttag('a', [('href', 'www.technovium.nl')])

        actual = str(self.sut.links.pop())
        expected = 'http://www.technovium.nl'
        self.assertEqual(actual, expected)

    def test_url_without_https_or_www(self):
        self.sut.handle_starttag('a', [('href', 'technovium.nl')])
        actual = str(self.sut.links.pop())
        expected = 'http://technovium.nl'
        self.assertEqual(actual, expected)

    def test_url_without_nl_domain(self):
        self.sut.handle_starttag('a', [('href', 'http://www.technovium.com')])
        actual = self.sut.links
        self.assertFalse(actual)

    def test_mailto(self):
        self.sut.handle_starttag('a', [('href', 'mailto:test@test.nl')])
        actual = self.sut.links
        self.assertFalse(actual)

    def test_http_http(self):
        self.sut.handle_starttag('a', [('href', 'http://http:')])
        actual = self.sut.links
        self.assertFalse(actual)

    def test_https(self):
        self.sut.handle_starttag('a', [('href', 'https://')])
        actual = self.sut.links
        self.assertFalse(actual)

    def test_http(self):
        self.sut.handle_starttag('a', [('href', 'http:')])
        actual = self.sut.links
        self.assertFalse(actual)

    def test_relative_url(self):
        self.sut.handle_starttag('a', [('href', '/over_ons')])
        expected = 'http://www.technovium.nl/over_ons'
        actual = str(self.sut.links.pop())
        self.assertEqual(actual, expected)

    def test_relative_url_starting_without_dash(self):
        self.sut.handle_starttag('a', [('href', 'over_ons.html')])
        expected = 'http://www.technovium.nl/over_ons.html'
        actual = str(self.sut.links.pop())
        self.assertEqual(actual, expected)

    def test_relative_url_starting_with_points(self):
        self.sut.page_url.url_string = 'http://www.technovium.nl/test/'
        self.sut.handle_starttag('a', [('href', '../over_ons')])
        expected = 'http://www.technovium.nl/over_ons'
        actual = str(self.sut.links.pop())
        self.assertEqual(actual, expected)

    def test_relative_url_starting_with_double_points_and_slashes(self):
        self.sut.page_url.url_string = 'http://www.technovium.nl/test/tweedetest/derdetest'
        self.sut.handle_starttag('a', [('href', '../../over_ons')])
        expected = 'http://www.technovium.nl/over_ons'
        actual = str(self.sut.links.pop())
        self.assertEqual(actual, expected)

    def test_double_relative_url(self):
        self.sut.page_url.url_string = 'http://www.technovium.nl/test/tweedetest/derdetest/vierdetest'
        self.sut.handle_starttag('a', [('href', '../../over_ons')])
        expected = 'http://www.technovium.nl/test/over_ons'
        actual = str(self.sut.links.pop())
        self.assertEqual(actual, expected)

    def test_blacklistnotfounderror_is_raised(self):
        Properties.BLACKLIST_FILE = 'Empty'
        with self.assertRaises(BlacklistNotFoundError):
            self.sut.handle_starttag('a', [('href', 'http://www.technovium.nl')])

    def test_error(self):
        with self.assertRaises(Exception):
            self.sut.error("testError")
