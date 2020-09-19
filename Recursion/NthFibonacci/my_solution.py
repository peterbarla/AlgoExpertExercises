# O(2^n) time | O(n) space
def getNthFib(n):
    if n == 1: return 0
    elif n < 4: return 1
    else:
        return getNthFib(n - 2) + getNthFib(n - 1)

print(getNthFib(4))
