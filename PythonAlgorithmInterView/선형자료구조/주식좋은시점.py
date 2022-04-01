def maxProfit(self, prices: list[int]) -> int:
    min_price = 10001
    max_price = 0

    for price in prices :
        min_price = min(min_price, price)
        max_price = max(max_price, price - min_price)

    return max_price



if __name__ == '__main__':
    # [7, 1, 5, 3, 6, 4]
    # prices = [7,6,4,3,1]
    prices = [7, 1, 5, 3, 6, 4]
    maxProfit(None, prices)
