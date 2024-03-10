
class IntersectionTwoArrays:

	def solution01(self, array1: list[int], array2: list[int]) -> list[int]:
		inter = set(array1) & set(array2)
		return list(inter)