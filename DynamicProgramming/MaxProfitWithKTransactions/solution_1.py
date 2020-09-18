# O(nk) time | O(n) space where n is the length of prices and k is the number of transactions
def maxProfitWithKTransactions(prices, k):
    if k < 1 or len(prices) < 2: return 0
    firstRow = [0 for i in range(len(prices))]
    secondRow = []
    for _ in range(k):
        secondRow = [0 for k in range(len(prices))]
        for j in range(1, len(prices)):
            maxProfitWithLessTransactions = getMaxProfit(firstRow, prices, j)
            secondRow[j] = max(secondRow[j - 1], prices[j] +  maxProfitWithLessTransactions)
        firstRow = secondRow[0:]

    return secondRow[-1]

def getMaxProfit(firstRow, prices, j):
    maxProfit = float('-inf')
    for i in range(0, j):
        maxProfit = max(maxProfit, firstRow[i] - prices[i])
    return maxProfit

prices = [5, 11, 3, 50, 60, 90]
k = 2

print(maxProfitWithKTransactions(prices, k))