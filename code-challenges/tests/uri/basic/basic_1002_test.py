import sys
sys.path.insert(0, './src/uri/basic')
import unittest

from basic_1002 import CircleArea

class TestCircleArea(unittest.TestCase):

    def setUp(self):
        self.test = CircleArea()

    def test_sum_numbers(self):
        self.assertEqual(self.test.solution(2.00), 'A=12.5664')
        self.assertEqual(self.test.solution(100.64), 'A=31819.3103')
        self.assertEqual(self.test.solution(150.00), 'A=70685.7750')

if __name__ == '__main__':
    unittest.main() 