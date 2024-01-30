
class TwoNumberSum:

    def solution01(self, array, targetSum):
        for i in range(len(array) - 1):
            for j in range(i + 1, len(array)):
                if (array[i] + array[j] == targetSum):
                    return [array[j], array[i]]
        return []

    def solution02(self, array, targetSum):
        array.sort()
        left = 0
        right = len(array) - 1

        while left < right:
            currentSum = array[left] + array[right]
            if currentSum == targetSum:
                return [array[left], array[right]]
            elif currentSum > targetSum:
                right -= 1
            else:
                left += 1
        return []

    def solution03(self, array, targetSum):
        nums = {}
        for number in array:
            match = targetSum - number
            if match in nums:
                return [match, number]
            else:
                nums[number] = True
        return []