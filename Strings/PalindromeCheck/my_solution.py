# O(n) time | O(1) space
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