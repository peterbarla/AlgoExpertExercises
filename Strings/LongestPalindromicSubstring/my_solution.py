# O(n^3) time | O(1) space
def longestPalindromicSubstring(string):
    longest_palindrome = ''
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i: j + 1]
            if len(substring) > len(longest_palindrome) and isPalindrome(substring):
                longest_palindrome = substring[0:]
    return longest_palindrome

def isPalindrome(string):
    if len(string) == 1: return True
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True
string = 'abaxyzzyxf'
print(longestPalindromicSubstring(string))