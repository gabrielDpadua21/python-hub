import sys
sys.path.insert(0, './src/uri/basic')
import unittest

from basic_1000 import HelloWorld

class TestHellorWord(unittest.TestCase):

    def setUp(self):
        self.change = HelloWorld()

    def test_hello_world(self):
        self.assertEqual(self.change.solution(), 'Hello World!')


if __name__ == '__main__':
    unittest.main()