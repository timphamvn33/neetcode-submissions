class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        [1, 2, 4, 6]
        [1, 1, 2, 8]
        [48, 24, 6, 1]

        [48, 24, 12, 8]
        prefix = []
        suffix = [1]*len(nums)
        results = []
        left_num = 1
        right_num = 1

        for num in nums:
            prefix.append(left_num)
            left_num *= num

        for n in range(len(nums) -1, -1, -1):
            suffix[n] = right_num
            right_num *= nums[n]
        
        # reverse the right_num
        
        for n_ in range(len(nums)):
            results.append(prefix[n_]*suffix[n_])
        return results



