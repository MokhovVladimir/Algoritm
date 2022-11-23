def getDescentPeriods(prices):
    dp = [1] * len(prices)
    g = len(prices)
    for i in range(1, len(prices)):
        if prices[i-1] - prices[i] == 1:
            dp[i] = dp[i-1] + 1

    return sum(dp)


print(getDescentPeriods([12,11,10,9,8,7,6,5,4,3,4,3,10,9,8,7]))