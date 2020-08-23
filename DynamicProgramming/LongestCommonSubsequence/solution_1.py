# O(nm) time | O(nm) space
def longestCommonSubsequence(str1, str2):
    lcs = [[[None, 0, None, None] for i in range(len(str1) + 1)] for j in range(len(str2) + 1)]

    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                lcs[i][j] = [str2[i - 1], lcs[i - 1][j - 1][1] + 1, i - 1, j - 1] 
            else:
                if lcs[i][j - 1][1] > lcs[i - 1][j][1]:
                    lcs[i][j] = [None, lcs[i][j - 1][1], i, j - 1]
                else:
                    lcs[i][j] = [None, lcs[i - 1][j][1], i - 1, j]


    result = []
    i = len(lcs) - 1
    j = len(lcs[0]) - 1
    while i != 0 and j != 0:
        curr = lcs[i][j]
        if curr[0] is not None:
            result.append(curr[0])
        i = curr[2]
        j = curr[3]

    return list(reversed(result))
str1 = "XKYKZPW"
str2 = "ZXVVYZW"

print(longestCommonSubsequence(str1, str2))