class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # input: piles = [1, 4, 3, 2]
        # K from 1 to max value in piles
        # ex: ks = [1, 2, 3, 4]
        # if we find the right k then total = 1/k + 4/k + 3/k + 2/k
        # naive solution can be loop thru the ks and apply that k into the formular of total if it equal to the h which is total then return k. But the time complexity will be O(n). 
        # using binary while iterate the ks will give better time compleity as O(logn)

        left = 1 # 1 is 1 hour
        right = max(piles)
        result = 1

        while left <= right:
            mid = (left + right) //2
            total = 0
            for pile in piles:
                total += math.ceil(pile/mid)
            if total <= h:
                result = mid
                right = mid - 1

            else:
                left = mid + 1
        return result


