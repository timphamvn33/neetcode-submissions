class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        nums_set = set(nums)

        for num in nums_set:
            if (num-1) not in nums_set:
                curr_len = 1
                while (num + 1) in nums_set:
                    curr_len += 1
                    num += 1
                max_len = max(max_len, curr_len)   
        return max_len


