#O(n)-best O(n)-avarage time | O(1) space
def bubbleSort(array):
    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                tmp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = tmp
                isSorted = False
        counter += 1
    return array