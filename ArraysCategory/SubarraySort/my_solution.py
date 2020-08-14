# O(n) time | O(n) space
def subarraySort(array):
    if(all(array[i] <= array[i + 1] for i in range(len(array) - 1))): 
        return [-1, -1]

    bad_start_index = -1
    bad_end_index = len(array) - 1
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            bad_start_index = i + 1
            break
            
    for i in range(len(array) - 1, 0, -1):
        if array[i] < array[i - 1]:
            bad_end_index = i
            break
    
    subarray = array[bad_start_index: bad_end_index + 1]

    lower_array = array[0:bad_start_index]
    upper_array = array[bad_end_index + 1:]

    print(lower_array, subarray, upper_array)
    
    if len(upper_array) != 0:
        min_from_upper = min(min(upper_array), min(subarray))
    else:
        min_from_upper = min(subarray)

    if len(lower_array) != 0:
        max_lower_array = max(max(lower_array), max(subarray))
    else:
        max_lower_array = max(subarray)

    true_starting_index_for_sort = bad_start_index
    true_ending_index_for_sort = bad_end_index

    for i in range(len(lower_array)):
        if lower_array[i] > min_from_upper:
            true_starting_index_for_sort = i
            break

    for i in range(len(upper_array)):
        if upper_array[i] < max_lower_array:
            true_ending_index_for_sort = i + len(lower_array) + len(subarray)

    print(true_starting_index_for_sort, true_ending_index_for_sort)

arr = [4, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 11, 57]


subarraySort(arr)