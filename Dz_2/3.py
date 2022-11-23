
def maxProfit(prices):
    if len(prices) > 1:
        sellbuy = [[0 for _ in range(len(prices))] for i in range(len(prices)-1)]
        for i in range(len(prices) - 1):
            for j in range(i+1, len(prices)):
                if i > 0 and prices[j] - prices[i] >= 0:
                    sellbuy[i][j] = max(sellbuy[i-1][:j]) + prices[j] - prices[i]
                elif i > 0 and prices[j] - prices[i] < 0:
                    sellbuy[i][j] = max(sellbuy[i - 1][:j])
                else:
                    sellbuy[i][j] = max(prices[j] - prices[i], 0)
        return sellbuy[-1][-1]
    return 0



