# O(n) time | O(1) space
def swap(list, pos1, pos2):
	list[pos1], list[pos2] = list[pos2], list[pos1]
	return list

def moveElementToEnd(array, toMove):
	
    number_of_swaps = 0
    for index in range(len(array)):
	    if array[index] != toMove and index > number_of_swaps:
		    array = swap(array, number_of_swaps, index)
		    number_of_swaps += 1
	
    return array