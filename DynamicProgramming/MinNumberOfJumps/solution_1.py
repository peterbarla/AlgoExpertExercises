# O(n) time | O(1) space
def minNumberOfJumps(array):
    max_reach = array[0]
    steps = array[0]
    jumps = 0
    if len(array) == 0 or len(array) == 1: return 0
    for i in range(1, len(array)):
        if i == len(array) - 1: return jumps + 1
        max_reach = max(max_reach, array[i] + i)
        steps -= 1
        if steps == 0:
            jumps += 1
            steps = max_reach - i