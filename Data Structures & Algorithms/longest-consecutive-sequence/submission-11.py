class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_l = 0
        set_nums = set(nums)
        [0, 1, 2, 3, 5, 6]
        [6, 5, 2, 1, 3, 0]

        for n in set_nums:
            if n - 1 not in set_nums:
                curr_len = 1
                np = n + 1
                while np in set_nums:
                    curr_len += 1
                    np += 1
                max_l = max(max_l, curr_len)
        return max_l


