# O(n^2) time | O(n^2) space
def fourNumberSum(array, targetSum):
    two_number_all_possible_sums = {}
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j:
                if (i, j) not in two_number_all_possible_sums and (j, i) not in two_number_all_possible_sums:
                    two_number_all_possible_sums[(i, j)] = [array[i], array[j]]
    

    results = []
    for item1, value1 in two_number_all_possible_sums.items():
        for item2, value2 in two_number_all_possible_sums.items():
            if item1 != item2:
                if value1[0] not in value2 and value1[1] not in value2:
                    if sum(value1) + sum(value2) == targetSum:
                        if sum(value1) + sum(value2) not in results:
                            arr = [value1[0], value1[1], value2[0], value2[1]]
                            arr.sort()
                            if arr not in results:
                                results.append(arr)

    return results
    



arr = [7, 6, 4, -1, 1, 2]
targSum = 16

print(fourNumberSum(arr, targSum))