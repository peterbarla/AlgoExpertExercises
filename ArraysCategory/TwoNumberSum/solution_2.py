# O(n) time | O(n) space
def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
	    if targetSum - num in nums:
		    return [num, targetSum - num]
	    else:
		    nums[num] = True
    return []