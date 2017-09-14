import unittest
from utils import JsonHelper


class JsonHelperTest(unittest.TestCase):

    def test_to_json(self):
        expected = '{"test": "test"}'
        value = {'test':'test'}
        self.assertEqual(expected, JsonHelper.to_json(value))

    def test_to_dict(self):
        expected = {'test': 'test'}
        value = JsonHelper.to_json({'test': 'test'})
        self.assertEqual(expected, JsonHelper.to_dict(value))
