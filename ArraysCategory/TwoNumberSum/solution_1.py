# O(nlog(n)) time | O(1) space
def twoNumberSum(array, targetSum):
	array.sort()
	left = 0
	right = len(array) - 1
	
	while array[left] < array[right]:
		potentialSum = array[left] + array[right]
		if potentialSum == targetSum:
			return [array[left], array[right]]
		elif potentialSum < targetSum:
			left += 1
		elif potentialSum > targetSum:
			right -= 1
	return []