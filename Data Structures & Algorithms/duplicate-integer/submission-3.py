class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for num in nums:
            nums_set.add(num)
        return len(nums_set) != len(nums)


























        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)

        # return False