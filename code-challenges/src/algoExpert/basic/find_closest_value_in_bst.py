class FindClosestValueInBst:

	# Average: Time O(Log(n)) | Space(Log(n))
	# Worst: Time O(n) | Space O(n)
	def solution01(self, tree, target):
		return self.findClosestValueHelper(tree, target, float("inf"))


	def solution02(self, tree, target):
		currentNode = tree
		closest = float("inf")

		while currentNode is not None:
			if abs(target - closest) > abs(target - currentNode.value):
				closest = currentNode.value
			if target < currentNode.value:
				currentNode = currentNode.left
			elif target > currentNode.value:
				currentNode = currentNode.right
			else:
				break

		return closest
		

	def findClosestValueHelper(self, tree, target, closest):
		
		if tree is None:
			return closest

		if abs(target - closest) > abs(target - tree.value):
			closest = tree.value

		if target < tree.value:
			return self.findClosestValueHelper(tree.left, target, closest)
		elif target > tree.value:
			return self.findClosestValueHelper(tree.right, target, closest)
		else:
			return closest

		

		