class NonConstructibleChange:

	# O(n log n) TIME | O(i) Space
	def solution01(self, coins):
		coins.sort()
		change = 0

		for coin in coins:
			if coin > change + 1:
				return change + 1

			change += coin

		return 1