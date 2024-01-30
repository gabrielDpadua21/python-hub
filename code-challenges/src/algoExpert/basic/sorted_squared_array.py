class SortedSqueredArray:

	def solution01(self, array):
		squared = []

		for number in array:
			squared.append(number ** 2)


		for i in range(len(squared)):
			for j in range(len(squared)):
				if squared[i] < squared[j]:
					aux = squared[i]
					squared[i] = squared[j]
					squared[j] = aux

		return squared


	def solution02(self, array):
		squared = [0] * len(array)
		start = 0
		end = len(array) - 1
		counter = len(array) - 1

		while end >= start:
			if abs(array[start]) > abs(array[end]):
				squared[counter] = (array[start] ** 2)
				start += 1
			else:
				squared[counter] = (array[end] ** 2)
				end -= 1
			counter -= 1




		return squared

	# O(n log n) time | O(n) space - complexity
	def solution03(self, array):
		squared = [0 for _ in array]

		for index in range(len(array)):
			squared[index] = array[index] ** 2

		squared.sort()

		return squared


	# O(n) time | O(n) space - complexity
	def solution04(self, array):
		squared = [0 for _ in array]
		small = 0
		large = len(array) - 1

		for index in reversed(range(len(array))):
			if abs(array[small]) > abs(array[large]):
				squared[index] = array[small] ** 2
				small += 1
			else:
				squared[index] = array[large] ** 2
				large -= 1


		return squared






