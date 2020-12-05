#O(n)-best O(n)-avarage time | O(1) space
import math
def selectionSort(array: list) -> list:
    sortedTill = 0
    for i in range(0, len(array) - 1):
        min = math.inf
        index = -1
        for j in range(sortedTill, len(array)):
            if array[j] < min:
                min = array[j]
                index = j
        swap(sortedTill, index, array)
        sortedTill += 1
    return array

def swap(i: int, j: int, array: list) -> None:
    array[i], array[j] = array[j], array[i]