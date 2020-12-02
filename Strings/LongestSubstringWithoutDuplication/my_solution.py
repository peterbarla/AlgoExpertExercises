
def longestSubstringWithoutDuplication(string):
    cache = {}
    longest_substr = []

    tmp_substr = []

    i = 0
    while i < len(string):
        letter = string[i]
        if letter not in cache:
            cache[letter] = i
            tmp_substr.append(letter)
            i += 1
        else:
            if len(tmp_substr) > len(longest_substr):
                longest_substr = tmp_substr[0:]
            tmp_substr = []
            i = cache[letter] + 1
            cache = {} 
    if len(tmp_substr) > len(longest_substr):
        longest_substr = tmp_substr[0:]
    return ''.join(longest_substr)

string = "clementisacap"

print(longestSubstringWithoutDuplication(string))
