class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums_set = set()
        # for num in nums:
        #     nums_set.add(num)
        # return len(nums_set) != len(nums)
        
        nums_hash = {}
        for i, num in enumerate(nums):
            if str(num) in nums_hash:
                return True
            nums_hash[str(num)] = i
        return False



























        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)

        # return False