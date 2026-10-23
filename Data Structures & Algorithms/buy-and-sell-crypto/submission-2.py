class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # first set the min_price value as the bigest infinities float
        # first set the max = 0
        # if price < min_price -> min_price = price
        # if (price - min_price) > price_max -> mprice_max = price-min_price
        # after all return 0
        # min_price = float('inf')
        # max_price = 0

        # for price in prices:
        #     if price < min_price:
        #         min_price = price
        #     elif (price - min_price) > max_price:
        #         max_price = (price - min_price)
        # return max_price 

        # using the sliding window
        left, right = 0, 1
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                max_profit = max(max_profit, (prices[right] - prices[left]))
                
            else:
                left = right
                    
            right += 1

        return max_profit
