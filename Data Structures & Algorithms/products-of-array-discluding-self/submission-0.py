class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # using the method production of all the left of i elemts x production of all the right of i element
        n = len(nums)
        results = [1] * n

        left = 1
        # List of production of all element the left of i
        for i in range(n):
            results[i] = left
            left *= nums[i]
            # return [1 1 2 8] 
                    #  [1, 2,4, 6]
                    #  []

        # list pf production of all element from the right of i
        right = 1
        for j in range(n-1, -1, -1):
            results[j]*= right #
            right *= nums[j]
        return results
        