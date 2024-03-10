import sys
sys.path.insert(0, '../../../src/leetcode')
import unittest

from easy.minimun_common_value import MinimunCommonValue


ARRAY1 = [1, 2, 3, 4, 6, 7, 9]
ARRAY2 = [-1, 5, 8, 9, 10, 12]
RESULT = 9


class TestMinimunCommonValue(unittest.TestCase):

	def setUp(self):
		self.find = MinimunCommonValue()


	def test_solution01(self):
		self.assertEqual(self.find.solution01(ARRAY1, ARRAY2), RESULT)




if __name__ == "__main__":
	unittest.main()