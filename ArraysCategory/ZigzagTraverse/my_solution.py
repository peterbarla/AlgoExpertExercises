# O(n) time | O(n) space
def zigzagTraverse(array):
    i, j = 0, 0
    number_of_elements_in_the_array = len(array) * len(array[0])
    result = []
    if number_of_elements_in_the_array != 0:
        result.append(array[i][j])
    added_elements = 1
    down = False
    up = True
    if len(array) > 1:
        i += 1
    else: j += 1
    while added_elements < number_of_elements_in_the_array:
        if up:
            if i == 0 or j == len(array[0]) - 1:
                result.append(array[i][j])
                added_elements += 1
                up = False
                down = True
                if j + 1 < len(array[0]):
                    j += 1
                else: i += 1
            else:
                result.append(array[i][j])
                added_elements += 1
                i -= 1
                j += 1
        elif down:
            if j == 0 or i == len(array) - 1:
                result.append(array[i][j])
                added_elements += 1
                up = True
                down = False
                if i + 1 < len(array):
                    i += 1
                else:
                    j += 1
            else:
                result.append(array[i][j])
                added_elements += 1
                i += 1
                j -= 1
    return result

'''arr = [  [1, 3, 4, 10, 3, 3], 
            [2, 5, 9, 11, 4, 4],
            [6, 8, 12, 15, 4, 4], 
            [7, 13, 14, 16, 4, 4]]'''

'''arr = [
    [1, 3, 4, 10, 11],
    [2, 5, 9, 12, 20],
    [6, 8, 13, 19, 21],
    [7, 14, 18, 22, 27],
    [15, 17, 23, 26, 28],
    [16, 24, 25, 29, 30]
  ]'''

arr = [[1, 2, 3, 4, 5]]

print(zigzagTraverse(arr))