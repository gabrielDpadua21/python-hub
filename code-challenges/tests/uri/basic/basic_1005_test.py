import sys
sys.path.insert(0, './src/uri/basic')
import unittest

from basic_1005 import SimpleMean

class TestSimpleMean(unittest.TestCase):

    def setUp(self):
        self.test = SimpleMean()

    def test_sum_numbers(self):
        self.assertEqual(self.test.solution(5.0, 7.1), 'MEDIA = 6.43182')
        self.assertEqual(self.test.solution(0.0, 7.1), 'MEDIA = 4.84091')
        self.assertEqual(self.test.solution(10.0, 10.0), 'MEDIA = 10.00000')

if __name__ == '__main__':
    unittest.main() 