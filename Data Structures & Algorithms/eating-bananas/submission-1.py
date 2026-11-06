class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # find the max pile
        # each hour koko eats each pile will be banana/k
        
        max_pile = 0
        result = -1

        for pile in piles:
            max_pile = max(max_pile, pile)
        
        left = 1
        right = max_pile
        while left <= right:
            mid = (left + right) // 2
            # ceil of pile/mid < 
            total = 0
            for pile in piles:
                total += (pile + mid -1) // mid
            
            if total <= h: 
               right = mid -1
               result = mid
            else:
                left = mid + 1
        return result

        