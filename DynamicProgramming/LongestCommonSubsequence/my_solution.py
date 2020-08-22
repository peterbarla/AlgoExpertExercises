def longestCommonSubsequence(str1, str2):
    current_row = ['' for i in range(len(str2) + 1)]
    last_row = ['' for i in range(len(str2) + 1)]

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                current_row[j] = last_row[j - 1] + str1[i - 1]
            else:
                current_row[j] = max(current_row[j - 1], last_row[j], key=len)
        last_row = current_row[0:]
    result = []
    for elem in last_row[-1]:
        result.append(elem)
    return result
str1 = "XKYKZPW"
str2 = "ZXVVYZW"

print(longestCommonSubsequence(str1, str2))