import sys
sys.path.insert(0, './src/algoExpert/basic')
import unittest

from sorted_squared_array import SortedSqueredArray

ARRAY = [-7, -3, 1, 9, 22, 30]
RESULT = [1, 9, 49, 81, 484, 900]

class TestSortedSquaredArray(unittest.TestCase):

	def setUp(self):
		self.squared = SortedSqueredArray()

	def test_solution01(self):
		self.assertEqual(self.squared.solution01(ARRAY), RESULT)

	def test_solution02(self):
		self.assertEqual(self.squared.solution02(ARRAY), RESULT)

	def test_solution03(self):
		self.assertEqual(self.squared.solution03(ARRAY), RESULT)

	def test_solution04(self):
		self.assertEqual(self.squared.solution04(ARRAY), RESULT)


if __name__ == '__main__':
	unittest.main()