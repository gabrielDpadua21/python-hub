import sys
sys.path.insert(0, './src/uri/basic')
import unittest

from basic_1008 import SimpleSalary

class TestSimpleSalary(unittest.TestCase):

    def setUp(self) -> None:
        self.test = SimpleSalary()

    def test(self):
        self.assertEqual(self.test.solution(25, 100, 5.50), 'SALARY = U$ 550.00')
        self.assertEqual(self.test.solution(1, 200, 20.50), 'SALARY = U$ 4100.00')
        self.assertEqual(self.test.solution(6, 145, 15.55), 'SALARY = U$ 2254.75')


if __name__ == '__main__':
    unittest.main()

