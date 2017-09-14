import unittest

from properties import Properties
from utils import CfgReader


class SettingsTest(unittest.TestCase):

    def setUp(self):
        Properties.MODULES_CONFIG_FILE = '../test/test_utils/test_my_module.conf'
        self.sut = CfgReader(Properties.MODULES_CONFIG_FILE)

    def test_get_section(self):
        expected = 3
        self.assertEqual(expected, len(self.sut.get_section('my.test.modules')))
