# O(n) time | O(n) space
def spiralTraverse(array):
    output_array = []
    fill_with_perimeters(array, 0, 0, len(array) - 1, len(array[0]) - 1, output_array)
    return output_array


def fill_with_perimeters(array, up_row_index, left_column_index, down_row_index, right_column_index, 
					  output_array):
    if left_column_index > right_column_index or up_row_index > down_row_index: return
    for i in range(left_column_index, right_column_index + 1):
	    output_array.append(array[up_row_index][i])

    for i in range(up_row_index, down_row_index):
        output_array.append(array[i + 1][right_column_index])
		
    for i in range(right_column_index, left_column_index, -1):
        if up_row_index != down_row_index:
	        output_array.append(array[down_row_index][i - 1])
		
    for i in range(down_row_index, up_row_index + 1, -1):
        if right_column_index != left_column_index:
	        output_array.append(array[i - 1][left_column_index])
		
    fill_with_perimeters(array, up_row_index + 1, left_column_index + 1, down_row_index - 1,
						right_column_index - 1, output_array)

arr = [ [1, 2, 3, 4], 
        [10, 11, 12, 5], 
        [9, 8, 7, 6]]
print(spiralTraverse(arr))