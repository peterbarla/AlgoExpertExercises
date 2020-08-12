# O(n) time | O(n) space
def spiralTraverse(array):
    right_steps = len(array[0])
    elements_visitted = 0
	
    total_number_of_elements = len(array)*len(array[0])
    output_array = []
	
    up_bound = 0
    right_bound = len(array[0]) - 1
    down_bound = len(array) - 1
    left_bound = 0
	
    current_round = 1
	
    while elements_visitted < total_number_of_elements:
	
	    down_steps = right_steps
	    left_steps = right_steps - 1
	    up_steps = right_steps - 1
		
	    for i in range(current_round - 1, right_steps):
		    output_array.append(array[up_bound][i])
		    elements_visitted += 1
			
	    for i in range(current_round, down_steps):
		    output_array.append(array[i][right_bound])
		    elements_visitted += 1
			
	    for i in range(left_steps - 1, current_round - 2, -1):
		    output_array.append(array[down_bound][i])
		    elements_visitted += 1
			
	    for i in range(up_steps - 1, current_round - 1, -1):
		    output_array.append(array[i][left_bound])
		    elements_visitted += 1
			
	    current_round += 1
	    right_steps -= 1
	    up_bound += 1
	    right_bound -= 1
	    down_bound -= 1
	    left_bound += 1

    print(elements_visitted, total_number_of_elements)
    return output_array


arr = [
    [19, 32, 33, 34, 25, 8],
    [16, 15, 14, 13, 12, 11],
    [18, 31, 36, 35, 26, 9],
    [1, 2, 3, 4, 5, 6],
    [20, 21, 22, 23, 24, 7],
    [17, 30, 29, 28, 27, 10]
  ]
print(spiralTraverse(arr))