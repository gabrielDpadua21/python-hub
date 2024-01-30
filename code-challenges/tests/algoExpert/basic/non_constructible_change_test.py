import sys
sys.path.insert(0, './src/algoExpert/basic')
import unittest


from non_constructible_change import NonConstructibleChange


COINS = [6, 4, 5, 1, 1, 8, 9]
RESULT = 3


class TestNonConstructibleChange(unittest.TestCase):

	def setUp(self):
		self.change = NonConstructibleChange()

	def test_solution01(self):
		self.assertEqual(self.change.solution01(COINS), RESULT)


if __name__ == '__main__':
	unittest.main()
