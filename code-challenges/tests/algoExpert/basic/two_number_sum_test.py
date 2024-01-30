import sys, os
sys.path.insert(0, './src/algoExpert/basic')
import unittest

from two_number_sum import TwoNumberSum

ARRAY_ELEMENTS = [3, 5, -4, 8, 11, 1, -1, 6]
TARGET_SUM = 10
RESULT = [-1, 11]

class TwoNumberSumTest(unittest.TestCase):

    def setUp(self):
        self.twoNumberSum = TwoNumberSum()


    def test_solution01(self):
        self.assertEqual(self.twoNumberSum.solution01(ARRAY_ELEMENTS, TARGET_SUM), RESULT)

    def test_solution02(self):
        self.assertEqual(self.twoNumberSum.solution02(ARRAY_ELEMENTS, TARGET_SUM), RESULT)

    def test_solution03(self):
        self.assertEqual(self.twoNumberSum.solution03(ARRAY_ELEMENTS, TARGET_SUM), RESULT)
    
if __name__ == '__main__':
    unittest.main()