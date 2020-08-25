# O(n^2) time | O(1) space
def longestPalindromicSubstring(string):
    longest_palindrome = [0, 1]
    for i in range(1, len(string)):
        odd = expand_from_index(string, i - 1, i + 1)
        even = expand_from_index(string, i - 1, i)
        tmp_longest = max(odd, even, key=lambda x : x[1] - x[0])
        longest_palindrome = max(longest_palindrome, tmp_longest, key=lambda x : x[1] - x[0])
    return string[longest_palindrome[0]: longest_palindrome[1]]

def expand_from_index(string, left, right):
    leftid = left
    rightid = right

    while leftid >= 0 and rightid < len(string):
        if string[leftid] != string[rightid]:
            break
        leftid -= 1
        rightid += 1

    return [leftid + 1, rightid]

string = 'abaxyzzyxf'
print(longestPalindromicSubstring(string))