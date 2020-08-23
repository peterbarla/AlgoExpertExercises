# O(n) time | O(n) space
def waterArea(heights):
    result_1 = [0 for i in range(len(heights))]
    if len(heights) <= 2: return 0
    for i in range(1, len(heights)):
        if heights[i] > result_1[i - 1]:
            result_1[i] = result_1[i - 1]
        else: result_1[i] = max(heights[i - 1], result_1[i - 1])
    
    result_2 = result_1[0:]
    result_2[-1] = heights[-1]
    for i in reversed(range(len(heights) - 1)):
        result_2[i] = max(heights[i + 1], result_2[i + 1])

    result = [min(i, j) for i, j in zip(result_1, result_2)]
    res = [i - j for i, j in zip(result, heights)]
    summ = 0
    for elem in res:
        if elem > 0:
            summ += elem
    return summ

arr = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
print(waterArea(arr))