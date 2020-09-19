# O(n) time | O(1) space
def getNthFib(n):
    first = 0
    second = 1
    number = 0
    if n == 1: return first
    elif n == 2: return second
    else:
        while n > 2:
            number = first + second
            first = second
            second = number
            n -= 1
    return number