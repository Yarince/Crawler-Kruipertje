import unittest

from utils.domain_parser import DomainParser


class DomainParserTest(unittest.TestCase):
    def setUp(self):
        self.sut = DomainParser()

    def test_get_domain_name(self):
        url = 'http://www.google.com'
        expected_domain = 'google.com'
        actual_domain = self.sut.get_domain_name(url)
        self.assertEqual(actual_domain, expected_domain)

    def test_except_get_domain_name_corrupt_url(self):
        url = 'google'
        expected_domain = ''
        actual_domain = self.sut.get_domain_name(url)
        self.assertEqual(expected_domain, actual_domain)

    def test_get_sub_domain_name_corrupt_url(self):
        url = 'google'
        expected_domain = ''
        actual_domain = self.sut.get_sub_domain_name(url)
        self.assertEqual(actual_domain, expected_domain)
