import sys
sys.path.insert(0, './src/algoExpert/basic')
import unittest

from tournament_winner import TournamentWinner


COMPETIONS = [
	['HTML', 'C#'],
	['C#', 'Python'],
	['Python', 'HTML']
]

RESULTS = [0, 0, 1]

WINNER = 'Python'


class TestTournamentWinner(unittest.TestCase):

	def setUp(self):
		self.tournament = TournamentWinner()

	def test_solution01(self):
		self.assertEqual(self.tournament.solution01(COMPETIONS, RESULTS), WINNER)

	def test_solution02(self):
		self.assertEqual(self.tournament.solution02(COMPETIONS, RESULTS), WINNER)

	def test_solution03(self):
		self.assertEqual(self.tournament.solution03(COMPETIONS, RESULTS), WINNER)

	def test_updateScores(self):
		self.assertEqual(self.tournament.updateScores('java', {}), None)



if __name__ == '__main__':
	unittest.main()


