# O(n^3) time | O(n) space
def fourNumberSum(array, targetSum):
    result_list = []
    array.sort()
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            left = j + 1
            right = len(array) - 1
            while left < right:
                if array[i] + array[j] + array[left] + array[right] == targetSum:
                    result_list.append([array[i], array[j], array[left], array[right]])
                    left += 1
                    right -= 1
                elif array[i] + array[j] + array[left] + array[right] < targetSum:
                    left += 1
                else:
                    right -= 1
                
    return result_list


arr = [7, 6, 4, -1, 1, 2]
targSum = 16

print(fourNumberSum(arr, targSum))
