class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        max_pro = 0
        for n in range(len(prices)):

            if prices[left] > prices[n]:
                left = n
            else:
                max_pro = max(max_pro,( prices[n]- prices[left]))
          

        return max_pro