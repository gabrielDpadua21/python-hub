import sys, os
sys.path.insert(0, './src/algoExpert/basic')
import unittest

from validate_subsequence import ValidateSubsequence

ARRAY = [5, 1, 22, 25, 6, -1, 8, 10]
SEQUENCE = [1, 6, -1, 10]
RESULT = True

class TestValidateSubsequence(unittest.TestCase):

    def setUp(self):
        self.validate = ValidateSubsequence()


    def test_solution01(self):
        self.assertEqual(self.validate.solution01(ARRAY, SEQUENCE), RESULT)

    def test_solution02(self):
        self.assertEqual(self.validate.solution02(ARRAY, SEQUENCE), RESULT)

    def test_soluction03(self):
        self.assertEqual(self.validate.solution03(ARRAY, SEQUENCE), RESULT)
    
if __name__ == '__main__':
    unittest.main()