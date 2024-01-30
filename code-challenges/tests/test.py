import sys, os
sys.path.insert(0, './src')
import unittest
from test import Test

class MyTest(unittest.TestCase):

    def setUp(self):
        self.test = Test()

    def test_sum(self):
        self.assertEqual(self.test.sum(2, 3), 4)

if __name__ == '__main__':
    unittest.main() 