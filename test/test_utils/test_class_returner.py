import unittest

from utils import ClassReturner


class ClassReturnerTest(unittest.TestCase):

    def setUp(self):
        self.sut = ClassReturner()

    def test_get_class(self):
        mod = 'my_parser.module_handler.my_modules.wordpress_module'
        kls_string = 'WordPressModule'
        kls = self.sut.get_class(mod, kls_string)
        instance = kls()
        self.assertIsInstance(instance, kls)

    def test_get_class_wrong_kls(self):
        mod = 'my_parsers'
        kls_string = 'wrongcls'
        kls = self.sut.get_class(mod, kls_string)
        self.assertFalse(kls)

    def test_get_class_wrong_module(self):
        mod = 'notexisting'
        kls_string = 'Spider'
        kls = self.sut.get_class(mod, kls_string)
        self.assertFalse(kls)
