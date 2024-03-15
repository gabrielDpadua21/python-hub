import unittest
import sys
sys.path.insert(0, '../../../src/leetcode')
from easy.roman_number import RomanNumber

ROMAN = 'MCMXCIV'
RESULT = 1994

class TestRomanNumber(unittest.TestCase):

    def setUp(self):
        self.romanNumber = RomanNumber()


    def test_solution01(self):
        result = self.romanNumber.romanToInt01(ROMAN)
        self.assertEqual(result, RESULT)

    def test_solution02(self):
        result = self.romanNumber.romanToInt02(ROMAN)
        self.assertEqual(result, RESULT)

if __name__ == '__main__':
    unittest.main()
