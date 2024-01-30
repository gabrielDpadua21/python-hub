import sys
sys.path.insert(0, './src/uri/basic')
import unittest

from basic_1003 import SimpleSum

class TestSimpleSum(unittest.TestCase):

    def setUp(self):
        self.test = SimpleSum()

    def test_sum_numbers(self):
        self.assertEqual(self.test.solution(30, 10), 'SOMA = 40')
        self.assertEqual(self.test.solution(-30, 10), 'SOMA = -20')
        self.assertEqual(self.test.solution(0, 0), 'SOMA = 0')

if __name__ == '__main__':
    unittest.main() 