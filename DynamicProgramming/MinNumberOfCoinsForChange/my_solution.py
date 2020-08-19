# O(nm) time | O(n) space where m = length(denoms)
def minNumberOfCoinsForChange(n, denoms):
    numbers = [0 for i in range(0, n + 1)]
    denoms.sort()
    for denom in denoms:
        for i in range(0, n + 1):
            if denom == i:
                numbers[i] = 1
            elif denom < i:
                if numbers[i%denom] != 0:
                    numbers[i] = min(1+ numbers[i - denom], numbers[i])
                elif i%denom == 0:
                    numbers[i] = int(i/denom)
            
    return numbers[-1]
n = 10
arr = [1, 3, 4]
print(minNumberOfCoinsForChange(n, arr))