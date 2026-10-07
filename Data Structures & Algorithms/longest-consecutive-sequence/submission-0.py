class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # using hash set to solve this problem. convert list to set then we use current_num and current_len_cons to track the current number and the length of the logest consecutive
        nums_set = set(nums)
        longest_len = 0
        for num in nums_set:
            if (num -1) not in nums_set:
                current_num = num
                current_len_cons = 1
                while (current_num + 1) in nums_set:
                    current_num += 1
                    current_len_cons += 1
                longest_len = max(longest_len, current_len_cons)
        return longest_len