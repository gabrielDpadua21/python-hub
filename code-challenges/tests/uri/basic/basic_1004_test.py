import sys
sys.path.insert(0, './src/uri/basic')
import unittest

from basic_1004 import SimpleProduct

class TestSimpleProduct(unittest.TestCase):

    def setUp(self):
        self.test = SimpleProduct()

    def test_sum_numbers(self):
        self.assertEqual(self.test.solution(3, 9), 'PROD = 27')
        self.assertEqual(self.test.solution(-30, 10), 'PROD = -300')
        self.assertEqual(self.test.solution(0, 9), 'PROD = 0')

if __name__ == '__main__':
    unittest.main() 