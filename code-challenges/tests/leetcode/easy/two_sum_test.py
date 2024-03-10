import sys
sys.path.insert(0, '../../../src/leetcode')
import unittest

from easy.two_sum import TwoSum

ARRAY = [3, 4, 2]
TARGET = 6
RESULT = [1, 2]

class TestTwoSum(unittest.TestCase):

	def setUp(self):
		self.find = TwoSum()

	def test_solution01(self):
		self.assertEqual(self.find.solution01(ARRAY, TARGET), RESULT)


	def test_solution02(self):
		self.assertEqual(self.find.solution02(ARRAY, TARGET), RESULT)


if __name__ == "__main__":
	unittest.main()