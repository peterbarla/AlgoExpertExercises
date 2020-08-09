# O(n) time | O(1) space
def isValidSubsequence(array, sequence):
    curr_index = -1
    for elem in sequence:
	    if elem not in array:
		    return False
	    else:
		    if array.index(elem) <= curr_index:
			    return False
		    else:
			    curr_index = array.index(elem)
			    array[curr_index] = -99
    return True