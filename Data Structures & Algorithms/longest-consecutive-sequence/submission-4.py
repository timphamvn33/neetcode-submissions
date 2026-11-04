class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # this solution wrong
        # nums_set = set()
        # cons = set()
        # cons_num = 1
        # curr_len_con = 1

        # if not nums:
        #     return 0
        # if len(nums) == 1:
        #     return 1
        # for num in nums:
        #     nums_set.add(num)
        # for num in nums:
        #     cons_num = num + 1
        #     if cons_num in nums_set:
        #         cons.add(num)
        #         cons.add(cons_num)
            
            
        # return max(curr_len_con, len(cons))

        # this solution is correct

        num_set = set(nums)
        longest_seq = 0
        for num in nums:
            if num - 1 not in num_set:
                curr_count = 0
                curr_num = num
                while curr_num in num_set:
                    curr_num += 1
                    curr_count += 1
                longest_seq = max(longest_seq, curr_count)
        return longest_seq
        
            
        