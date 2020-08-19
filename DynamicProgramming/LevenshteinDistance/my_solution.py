# O(nm) time | O(min(n, m)) space
def levenshteinDistance(str1, str2):
    str1_array = [i for i in range(len(str1) + 1)]
    str2_array = [i for i in range(len(str2) + 1)]
    
    last_array = str2_array[0:]
    curr_array = [0 for i in range(len(str2_array))]
    i = 0
    while i < len(str1):
        curr_array[0] = str1_array[i + 1]
        for j in range(1, len(str2_array)):
            if str1[i] == str2[j - 1]:
                curr_array[j] = last_array[j - 1]
            else:
                curr_array[j] = min(min(curr_array[j - 1], last_array[j - 1]), last_array[j]) + 1
        last_array = curr_array[0:]
        i += 1

    return last_array[-1]

    


str1 = 'abc'
str2 = 'yabd'

print(levenshteinDistance(str1, str2))