import unittest

from domain import Url


class UrlTest(unittest.TestCase):

    def setUp(self):
        self.sut = Url("test_name", 0)

    def test_init(self):
        expected = "test_name", 0
        result = self.sut.url_string, self.sut.layer
        self.assertEquals(expected, result)

    def test___str__(self):
        expected = "test_name"
        result = str(self.sut)
        self.assertEquals(expected, result)

    def test___eq___positive(self):
        positive = Url("test_name")
        self.assertTrue(self.sut.__eq__(positive))
        negative_url = Url("Different name")
        self.assertFalse(self.sut.__eq__(negative_url))
        negative_non_url = 'Different class'
        self.assertFalse(self.sut.__eq__(negative_non_url))

    def test___ne__(self):
        negative_non_url = 'Different class'
        self.assertTrue(self.sut.__ne__(negative_non_url))
