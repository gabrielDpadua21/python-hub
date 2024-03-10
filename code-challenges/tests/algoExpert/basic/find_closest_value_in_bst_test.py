import sys
sys.path.insert(0, '../../../src/algoExpert')
import unittest

from basic.find_closest_value_in_bst import FindClosestValueInBst
from classes.bst import Bst


TARGET = 12

RESULT = 13


class TestFindClosestValueInBst(unittest.TestCase):

	def setUp(self):
		self.find = FindClosestValueInBst()

	def treeMount(self):
		root = Bst(10)
		root.left = Bst(5)
		root.left.left = Bst(2)
		root.left.left.left = Bst(1)
		root.left.right = Bst(5)
		root.right = Bst(15)
		root.right.left = Bst(13)
		root.right.left.right = Bst(14)
		root.right.right = Bst(22)
		return root


	def test_solution01(self):
		tree = self.treeMount()
		self.assertEqual(self.find.solution01(tree, TARGET), RESULT)

	def test_solution02(self):
		tree = self.treeMount()
		self.assertEqual(self.find.solution02(tree, TARGET), RESULT)


if __name__ == '__main__':
	unittest.main()