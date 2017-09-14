import unittest

from test.mock.mythread_mock import MyThreadMock
from utils import MyThread


class MyThreadTest(unittest.TestCase):
    def setUp(self):
        self.sut = MyThread(None, MyThreadMock())

    def test_mythread_is_initialized(self):
        expected = "MyThreadMock-1"
        actual = self.sut.name
        self.assertEqual(expected, actual)
