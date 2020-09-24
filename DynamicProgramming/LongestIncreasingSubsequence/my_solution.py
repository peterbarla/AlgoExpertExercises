# O(n^2) time | O(n) space
def longestIncreasingSubsequence(array):
    lengths = [0 for i in range(len(array))]
    lengths[0] = 1

    sequences = [0 for i in range(len(array))]
    sequences[0] = None
    for i in range(1, len(array)):
        getFirstSmallerBeforeNumber(i, array, lengths, sequences)
    result = buildSequence(lengths, sequences, array)
    result.reverse()
    return result
        
def getFirstSmallerBeforeNumber(index, array, lengths, sequences):
    found = False
    for i in range(0, index):
        if array[i] < array[index]:
            if lengths[index] < lengths[i] + 1:
                lengths[index] = lengths[i] + 1
                sequences[index] = i
            found = True
    if not found:
        lengths[index] = 1
        sequences[index] = None

def buildSequence(lengths, sequences, array):
    result = []
    startingIndex = lengths.index(max(lengths))
    while startingIndex != None:
        result.append(array[startingIndex])
        tmp = startingIndex
        startingIndex = sequences[tmp]
    return result

array = [5, 7, -24, 12, 10, 2, 3, 2, 12, 5, 6, 35]
print(longestIncreasingSubsequence(array))