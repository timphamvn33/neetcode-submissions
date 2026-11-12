class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # [1, 4, 3, 2]
        # []
        # [1, 2, 2, 1] 2

        # need to find the minimum result but koko can spend to eat each banana in all piles less than h

        # will find the result from 1 to max banana
        [1, 2, 3, 4]

        max_ba = 0
        for p in piles:
            max_ba = max(max_ba, p)
        left = 1

        right = max_ba
        result = -1

        while left <= right:
            mid = (left + right) // 2
            hour_eat = 0
            for p in piles:
                hour_eat += (p + mid - 1) // mid

            if hour_eat <= h: # need to make this bigger so move the right to mid -1
                right = mid -1
                result = mid
            else: # need to make hour_eat smaller then move left to the mid + 1
                left = mid + 1
        return result


                
        
            
                
                
