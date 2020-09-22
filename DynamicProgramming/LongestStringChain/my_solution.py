# O(n*m^2 + nlog(n)) time | O(n) space
def longestStringChain(strings):
    strings.sort(key=len)
    cache = {}
    for string in strings:
        cache[string] = {'smallerString': "", 'chainSize': 1}
    for string in strings:
        buildLongestStringChain(string, cache)
    return getLongestChain(cache, strings)


def buildLongestStringChain(string, cache):
    for i in range(len(string)):
        curr_string = string[0:i] + string[i + 1:]
        if curr_string in cache:
            updateLongestStringChain(string, curr_string, cache)

def updateLongestStringChain(string, curr_string, cache):
    if cache[curr_string]['chainSize'] + 1 > cache[string]['chainSize']:
        cache[string]['smallerString'] = curr_string
        cache[string]['chainSize'] = 1 + cache[curr_string]['chainSize']

def getLongestChain(cache, strings):
    length = 0
    start_string = ''
    for string in strings:
        if cache[string]['chainSize'] > length:
            length = cache[string]['chainSize']
            start_string = string
    if length == 1: return []
    curr_string = start_string
    result = []
    while curr_string != '':
        result.append(curr_string)
        curr_string = cache[curr_string]['smallerString']
    return result

strings = ["abde", "abc", "abd", "abcde", "ade", "ae", "1abde", "abcdef"]

print(longestStringChain(strings))