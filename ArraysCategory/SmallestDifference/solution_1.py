# O(nlog(n) + mlog(m)) space | O(1) time
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
	
    left_one = 0
	left_two = 0
	
	num_one = 99
	num_two = 99
	diff = float('inf')
	
	while left_one < len(arrayOne) and left_two < len(arrayTwo):
		if arrayOne[left_one] == arrayTwo[left_two]:
			num_one = arrayOne[left_one]
			num_two = arrayTwo[left_two]
			diff = abs(arrayOne[left_one] - arrayTwo[left_two])
			break
		elif arrayOne[left_one] < arrayTwo[left_two]:
			if abs(arrayOne[left_one] - arrayTwo[left_two]) < diff:
				num_one = arrayOne[left_one]
				num_two = arrayTwo[left_two]
				diff = abs(arrayOne[left_one] - arrayTwo[left_two])
			left_one += 1
		else:
			if abs(arrayOne[left_one] - arrayTwo[left_two]) < diff:
				num_one = arrayOne[left_one]
				num_two = arrayTwo[left_two]
				diff = abs(arrayOne[left_one] - arrayTwo[left_two])
			left_two += 1
    return [num_one, num_two]
