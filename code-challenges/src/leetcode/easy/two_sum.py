

class TwoSum():

	def solution01(self, nums: list[int], target: int) -> list[int]:
		size = len(nums)
		for index in range(size):
			for index2 in range(size):
				if (index != index2) and nums[index] + nums[index2] == target:
					return [index, index2]
		return []


	def solution02(self, nums: list[int], target: int) -> list[int]:
		num_index = {} 

		for index, num in enumerate(nums):
			diference = target - num

			if diference in num_index:
				return [num_index[diference], index]

			num_index[num] = index
