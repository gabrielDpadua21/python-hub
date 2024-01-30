import sys
sys.path.insert(0, './src/uri/basic')
import unittest

from basic_1006 import PonderedMean

class TestPonderedMean(unittest.TestCase):

    def setUp(self) -> None:
        self.test = PonderedMean()

    def test(self):
        self.assertEqual(self.test.solution(5.0, 6.0, 7.0), 'MEDIA = 6.3')
        self.assertEqual(self.test.solution(5.0, 10.0, 10.0), 'MEDIA = 9.0')
        self.assertEqual(self.test.solution(10.0, 10.0, 5.0), 'MEDIA = 7.5')

if __name__ == '__main__':
    unittest.main()
