import sys
sys.path.insert(0, '../../../src/leetcode')
import unittest

from easy.palindrome_number import PalindromeNumber

NUMBER = -121
RESULT = False

class TestTwoSum(unittest.TestCase):

	def setUp(self):
		self.find = PalindromeNumber()

	def test_solution01(self):
		self.assertEqual(self.find.solution01(NUMBER), RESULT)


	def test_solution02(self):
		self.assertEqual(self.find.solution02(NUMBER), RESULT)


if __name__ == "__main__":
	unittest.main()