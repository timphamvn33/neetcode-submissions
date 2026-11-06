class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        result_max_len = 0
        # chek if num -1 not in nums_set then start count the sequence in the nums_set
        for num in nums:
            num_prev = num - 1
            if num_prev not in nums_set:
                nums_seq_len = 0
                while num in nums_set:
                    nums_seq_len += 1
                    num += 1
                result_max_len = max(result_max_len, nums_seq_len)
        return result_max_len
                
                

            

            

