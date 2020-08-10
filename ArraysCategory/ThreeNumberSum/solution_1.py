# O(n^2) time | O(n) space
def threeNumberSum(array, targetSum):
    result_triplets = []
    array.sort()
    for index in range(len(array) - 2):
	    left = index + 1
	    right = len(array) - 1
		
	    while left < right:
		    if array[index] + array[left] + array[right] == targetSum:
			    result_triplets.append([array[index], array[left], array[right]])
			    left += 1
			    right -= 1
		    elif array[index] + array[left] + array[right] < targetSum:
			    left += 1
		    elif array[index] + array[left] + array[right] > targetSum:
			    right -= 1
				
    return result_triplets