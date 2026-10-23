class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # first set the min_price value as the bigest infinities float
        # first set the max = 0
        # if price < min_price -> min_price = price
        # if (price - min_price) > price_max -> mprice_max = price-min_price
        # after all return 0
        min_price = float('inf')
        max_price = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif (price - min_price) > max_price:
                max_price = (price - min_price)
        return max_price 