# O(n^2) time | O(1) space
def largestRange(array):
    
    
    min_elem = min(array)
    max_elem = max(array)
    
    result = [min_elem, min_elem]
    tmp = [min_elem, min_elem]
    for elem in range(min_elem + 1, max_elem + 1):
        if elem in array:
            tmp[1] = elem
        else:
            distance_result = result[1] - result[0]
            distance_tmp = tmp[1] - tmp[0]
            if distance_tmp > distance_result:
                result = tmp[0:]
            tmp.clear()
            tmp.append(elem + 1)
            tmp.append(elem + 1)
        if elem == max_elem:
            distance_result = result[1] - result[0]
            distance_tmp = tmp[1] - tmp[0]
            if distance_tmp > distance_result:
                result = tmp[0:]
    return result
