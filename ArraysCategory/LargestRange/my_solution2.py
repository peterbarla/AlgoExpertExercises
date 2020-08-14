# O(n) time | O(n) space
def largestRange(array):
    elements = {}
    for elem in array:
        elements[elem] = True
        
    result_range = []
    tmp_range = []
    
    for elem in array:
        if elem not in result_range:
            left_range = []
            middle_range = [elem]
            right_range = []
            tmp_elem = elem
            while tmp_elem - 1 in elements:
                left_range.append(tmp_elem - 1)
                tmp_elem = tmp_elem - 1
            tmp_elem = elem
            while tmp_elem + 1 in elements:
                right_range.append(tmp_elem + 1)
                tmp_elem = tmp_elem + 1

            tmp_range = left_range + middle_range + right_range
            tmp_range.sort()

            if len(tmp_range) > len(result_range):
                result_range = tmp_range[0:]
        
    return [result_range[0], result_range[-1]]

arr = [4, 2, 1, 3]

print(largestRange(arr))
