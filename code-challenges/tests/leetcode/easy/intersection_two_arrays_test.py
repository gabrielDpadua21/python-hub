import sys
sys.path.insert(0, '../../../src/leetcode')
import unittest

from easy.intersection_two_arrays import IntersectionTwoArrays

ARRAY1 = [3, 4, 2]
ARRAY2 = [5, 4, 2]
RESULT = [2, 4]

class TestTwoSum(unittest.TestCase):

	def setUp(self):
		self.find = IntersectionTwoArrays()

	def test_solution01(self):
		self.assertEqual(self.find.solution01(ARRAY1, ARRAY2), RESULT)


if __name__ == "__main__":
	unittest.main()