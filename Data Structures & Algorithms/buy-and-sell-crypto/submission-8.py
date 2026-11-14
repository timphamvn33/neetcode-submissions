class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_re = 0
        for i in range(len(prices)):
            if prices[left] >= prices[i]:
                left = i
            else:
                max_re = max(max_re, prices[i]- prices[left])
        return max_re
