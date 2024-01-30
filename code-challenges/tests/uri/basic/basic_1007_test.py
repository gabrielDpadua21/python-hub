import sys
sys.path.insert(0, './src/uri/basic')
import unittest

from basic_1007 import SimpleDiference

class TestSimpleDiference(unittest.TestCase):

    def setUp(self) -> None:
        self.test = SimpleDiference()

    def test(self):
        self.assertEqual(self.test.solution(5, 6, 7, 8), 'DIFERENCA = -26')
        self.assertEqual(self.test.solution(0, 0, 7, 8), 'DIFERENCA = -56')
        self.assertEqual(self.test.solution(5, 6, -7, 8), 'DIFERENCA = 86')

if __name__ == '__main__':
    unittest.main()
