# O(n) time | O(d) space where d is the greatest depth
def productSum(array, depth=1, idx=0):
    result = 0
    for elem in array:
        if type(elem) is list:
            result += (depth + 1) * productSum(elem, depth + 1, 0)
        else: result += elem
    return result
array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]

print(productSum(array))