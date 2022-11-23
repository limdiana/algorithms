def maxProfit(prices):
    maxprofit = [0] * len(prices)
    mini = prices[0]
    for i in range(1, len(prices)):
        maxprofit[i] = max(0, prices[i] - mini)
        if prices[i] < mini:
            mini = prices[i]
    return max(maxprofit)

print(maxProfit([7, 2, 6, 3, 4,]))
