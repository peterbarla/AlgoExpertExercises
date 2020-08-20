# O(n^2) time | O(n) space
def maxSumIncreasingSubsequence(array):
    sums = [array[i] for i in range(len(array))]
    sequences = [None for i in range(len(array))]
    if max(array) <= 0: return [max(array), [max(array)]]
    for i in range(len(array)):
        for j in range(0, i):
            if array[j] < array[i] and sums[j] + array[i] >= sums[i]:
                sums[i] = array[i] + sums[j]
                sequences[i] = j
    result = []
    id = sums.index(max(sums))
    while id is not None:
        result.append(array[id])
        id = sequences[id]
    return [max(sums), list(reversed(result))]