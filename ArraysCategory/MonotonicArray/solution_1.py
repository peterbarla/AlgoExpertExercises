def isMonotonic(array):
    inc = True
    dec = True
	
    for index in range(1, len(array)):
	    if array[index] < array[index - 1]:
		    inc = False
	    if array[index] > array[index - 1]:
		    dec = False
			
    return inc or dec
