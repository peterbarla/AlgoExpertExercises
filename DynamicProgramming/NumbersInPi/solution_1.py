# O(n^3 + m) time | O(n + m) space
def numbersInPi(pi, numbers):
    numbersTable = {number: True for number in numbers}
    minSpaces = calcMin(pi, numbersTable, {}, 0)
    return -1 if minSpaces == float('inf') else minSpaces
        
def calcMin(pi, numbersTable, cache, idx):
    if idx == len(pi):
        return -1
    if idx in cache:
        return cache[idx]
    minSpaces = float('inf')
    for i in range(idx, len(pi)):
        prefix = pi[idx: i + 1]
        if prefix in numbersTable:
            minSpaceSufix = calcMin(pi, numbersTable, cache, i + 1)
            minSpaces = min(minSpaces, minSpaceSufix + 1)
    cache[idx] = minSpaces
    return cache[idx]