""" Задача решена динамическим программированием."""
def maxProfit(prices):
    if len(prices) > 1:
        sellbuy = [[0 for _ in range(len(prices))] for i in range(len(prices)-1)]  # Создаем двумерный список, равный prices
        for i in range(len(prices) - 1):
            for j in range(i+1, len(prices)):
                if i > 0 and prices[j] - prices[i] >= 0:  # Если продавать в этот день выгодно и не первый день
                    sellbuy[i][j] = max(sellbuy[i-1][:j]) + prices[j] - prices[i]  # Берем максимальную прибыль в прошлые дни и суммириуем нашу прибыль

                elif i > 0 and prices[j] - prices[i] < 0:  # Если покупать невыгодно и у нас не первый день
                    sellbuy[i][j] = max(sellbuy[i - 1][:j])  # Берем максимальную выгоду за пердыдущие дни

                else:  # Если первый день, то порверяем чтоб список корректно заполнился в начале
                    sellbuy[i][j] = max(prices[j] - prices[i], 0)
        return sellbuy[-1][-1]  # максимальный элемент будет в конце
    return 0



