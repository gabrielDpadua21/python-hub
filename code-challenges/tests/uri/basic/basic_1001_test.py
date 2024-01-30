import sys
sys.path.insert(0, './src/uri/basic')
import unittest

from basic_1001 import SumNumbers

class TestSumNumbers(unittest.TestCase):

    def setUp(self):
        self.test = SumNumbers()

    def test_sum_numbers(self):
        self.assertEqual(self.test.solution(10, 9), 'X = 19')
        self.assertEqual(self.test.solution(-10, 4), 'X = -6')
        self.assertEqual(self.test.solution(15, -7), 'X = 8')

if __name__ == '__main__':
    unittest.main() 