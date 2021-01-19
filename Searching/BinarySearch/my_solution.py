# O(log(n)) time | O(1) space
def binarySearch(array, target):
	return searchBinary(array, target, 0, len(array) - 1)
	
def searchBinary(array: list, target: int, left: int, right: int) -> int:
	if left > right: return -1
	mid = (left + right) // 2
	potentialElem = array[mid]
	
	if target == potentialElem:
		return mid
	elif target > potentialElem:
		return searchBinary(array, target, mid + 1, right)
	else: return searchBinary(array, target, left, mid - 1)