def isMonotonic(array):
    if len(array) == 0: return True
	
    increasing_sum = array[0]
    decreasing_sum = array[0]
	
    increasing_type = False
    decreasing_type = False
	
    for index in range(1, len(array)):
	    if not increasing_type and not decreasing_type:
		    if array[index] == increasing_sum == decreasing_sum:
			    continue
		    elif array[index] > increasing_sum:
			    increasing_type = True
			    increasing_sum = array[index]
		    else:
			    decreasing_type = True
			    decreasing_sum = array[index]
			
	    if increasing_type:
		    if array[index] < increasing_sum:
			    return False
		    else:
			    increasing_sum = array[index]
	    elif decreasing_type:
		    if array[index] > decreasing_sum:
			    return False
		    else:
			    decreasing_sum = array[index]
    return True
