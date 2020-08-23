# O(n) time | O(n) space
def minNumberOfJumps(array):
    number_of_jumps = 0
    i = 0
    while i < len(array) - 1:
        if array[i] + i >= len(array) - 1:
            return number_of_jumps + 1
        possible_elems = array[i + 1: i + array[i] + 1]
        step_sum = i + array[i]
        index_to_step = i + array[i]
        for j in range(len(possible_elems)):
            if  possible_elems[j] + (i + j + 2 - (i + 1)) >= len(array)  - (i + 1):
                return number_of_jumps + 2
            if i + 1 + possible_elems[j] > len(array) - 1:
                return number_of_jumps + 2
            if possible_elems[j] + array[i + 1 + possible_elems[j]] > step_sum:
                step_sum = possible_elems[j] + array[i + 1 + possible_elems[j]]
                index_to_step = i + (j + 1)
        i = index_to_step
        number_of_jumps += 1
    return number_of_jumps



arr = [3, 10, 2, 1, 2, 3, 7, 1, 1, 1, 3, 2, 3, 2, 1, 1, 1, 1]
print(minNumberOfJumps(arr))