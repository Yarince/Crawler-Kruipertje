from unittest import TestCase
from app.crawler import URLHelper
from domain import Url


class TestURLHelper(TestCase):

    def test_url_in_urlset_true(self):
        url1 = Url('http://www.google.nl', 1)
        url2 = Url('http://www.google.nl', 1)
        urlset = set()
        urlset.add(url1)
        self.assertTrue(URLHelper.url_in_urlset(url2, urlset))

    def test_url_in_urlset_false(self):
        url1 = Url('http://www.google.nl', 1)
        url2 = Url('http://www.han.nl', 1)
        urlset = set()
        urlset.add(url1)
        self.assertFalse(URLHelper.url_in_urlset(url2, urlset))


