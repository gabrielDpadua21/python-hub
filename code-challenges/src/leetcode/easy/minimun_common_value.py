

class MinimunCommonValue:

	def solution01(self, array1, array2):
		inter = set(array1).intersection(set(array2))
		return min(inter) if len(inter) > 0 else 0