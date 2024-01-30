import operator

WINNER_POINTES = 3

class TournamentWinner:

	def solution01(self, competions, results):

		winners = {}

		for index in range(len(competions)):
			winnerIndex = 0

			if results[index] == 0:
				winnerIndex = 1

			if competions[index][winnerIndex] in winners:
				winners[competions[index][winnerIndex]] += 3
			else:
				winners[competions[index][winnerIndex]] = 3

		return max(winners.items(), key=operator.itemgetter(1))[0]


	def solution02(self, competions, results):
		score = {}
		winner = ""

		score[winner] = 0

		for index in range(len(competions)):
			winnerIndex = 0

			if results[index] == 0:
				winnerIndex = 1

			if competions[index][winnerIndex] in score:
				score[competions[index][winnerIndex]] += 3
			else:
				score[competions[index][winnerIndex]] = 3

			if score[winner] < score[competions[index][winnerIndex]]:
				winner = competions[index][winnerIndex]

		return winner


	# 0(n) time | O(k) space
	def solution03(self, competions, results):
		winner = ""

		scores = {winner: 0}

		for index, competion in enumerate(competions):
			result = results[index]
			homeTeam, awayTeam = competion

			winnerTeam = homeTeam if result == 1 else awayTeam

			self.updateScores(winnerTeam, scores)

			if scores[winnerTeam] > scores[winner]:
				winner = winnerTeam

		return winner
		


	def updateScores(self, winner, scores):
		if winner not in scores:
			scores[winner] = 0

		scores[winner] += 3

