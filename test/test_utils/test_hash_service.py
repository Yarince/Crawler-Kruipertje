import unittest

from utils import HashService


class HashServiceTest(unittest.TestCase):
    def setUp(self):
        self.sut = HashService()

    def test_md5(self):
        expected = '098f6bcd4621d373cade4e832627b4f6'
        actual = self.sut.md5('test')
        self.assertEqual(expected, actual)

    def test_num_md5(self):
        expected = 12707736894140473154801792860916528374
        actual = self.sut.num_md5('test')
        self.assertEqual(expected, actual)

    def test_num_md5_is_int(self):
        actual = self.sut.num_md5('test')
        self.assertIsInstance(actual, int)
