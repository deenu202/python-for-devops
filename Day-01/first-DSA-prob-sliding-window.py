def maxProfit(prices):
    l = 0
    max_profit = 0

    for r in range(len(prices)):
        if prices[l] < prices[r]:
            profit = prices[r] - prices [l]
            max_profit = max(max_profit, profit)
        else:
            l = r
    return max_profit

prices = list(map(int, input("Enter prices separated by spaces: ").split()))

print(maxProfit(prices))