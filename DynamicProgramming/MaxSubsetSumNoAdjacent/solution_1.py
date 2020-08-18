# o(n) time | O(1) space
def maxSubsetSumNoAdjacent(array):
    if len(array) == 0: return 0
    elif len(array) == 1: return array[0]
    elif len(array) == 2: return max(array[0], array[1])
    before_last_max = array[0]
    last_max = max(array[0], array[1])
    final_max = last_max

    
    i = 2
    while i < len(array):
        final_max = max(last_max, before_last_max + array[i])
        before_last_max = last_max
        last_max = final_max
        i +=1
        
    return final_max
arr = [75, 105, 120, 75, 90, 135]
print(maxSubsetSumNoAdjacent(arr))