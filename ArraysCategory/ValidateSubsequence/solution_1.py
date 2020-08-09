# O(n) time | O(1) space
def isValidSubsequence(array, sequence):
    seq_index = 0
	
    for elem in array:
	    if seq_index == len(sequence):
		    break
	    if elem == sequence[seq_index]:
		    seq_index += 1
			
    return seq_index == len(sequence)