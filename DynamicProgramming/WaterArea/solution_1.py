def waterArea(heights):
	if len(heights) <= 2: return 0
	left_index = 0
	right_index = len(heights) - 1
	left_most_height = heights[left_index]
	right_most_height = heights[right_index]
	summ = 0
	while left_index < right_index:
		if heights[left_index] < heights[right_index]:
			left_index += 1
			left_most_height = max(left_most_height, heights[left_index])
			summ += left_most_height - heights[left_index]
		else:
			right_index -= 1
			right_most_height = max(right_most_height, heights[right_index])
			summ += right_most_height - heights[right_index]
			
	return summ

arr = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
print(waterArea(arr))