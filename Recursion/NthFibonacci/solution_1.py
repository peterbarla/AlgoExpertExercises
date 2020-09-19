# O(n) time | O(n) space
def getNthFib(n, cache={1: 0, 2: 1}):
    if n == 1: return 0
    elif n < 4: return 1
    else:
        if n in cache:
            return cache[n]
        else:
            cache[n] = getNthFib(n - 2, cache) + getNthFib(n - 1, cache)
            return cache[n]