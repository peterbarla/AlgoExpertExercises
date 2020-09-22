# O(n^3) time | O(n) space
def palindromePartitioningMinCuts(string):
    cuts = [float('inf') for i in range(len(string))]
    palindromes = [False for i in range(len(string))]
    cuts[0] = 1       

    for i in range(1, len(string)):
        for j in range(0, i):
            if isPalindrome(string[j: i + 1]):
                palindromes[i] = True
                if palindromes[j]:
                    cuts[i] = min(cuts[i], cuts[j] + 1)
                else:
                    cuts[i] = min(cuts[i], cuts[j])
            else:
                cuts[i] = min(cuts[i], cuts[i - 1] + 1)
    return (cuts[-1] - 1)

def isPalindrome(string):
    return string == string[::-1]

string = "ababbbabbababa"
print(palindromePartitioningMinCuts(string))