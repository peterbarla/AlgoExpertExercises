#O(n)-best O(n)-avarage time | O(1) space
def insertionSort(array: list) -> list:
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap(j, j - 1, array)
            j -= 1
    return array

def swap(i: int, j: int, array: list) -> None:
    array[i], array[j] = array[j], array[i]