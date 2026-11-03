class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using hasmash to solve this problem.
        # if the target minus to one of the element and that value not seen in that hash map then add that (value, index) into the hashmap else return that element index and the element found in set

        # left, right = 0, 1

        # while left < right:
        #     target_exp = nums[left] + nums[right]
        #     if target_exp == target:
        #         return [left, right]
        #     else:
        #         right += 1
        #     if right == len(nums) -1:
        #         left += 1
        #         right = left + 1

        # return []

        set = {}

        for i, num in enumerate(nums):
            
            exp = target - num
            if exp in set:
                return [set[exp], i]
            set[num]= i
            
        return []
        
             


        




















        # seen = {}

        # for i, value in enumerate(nums):
        #     result_check = target - value
        #     if result_check in seen:
        #         return [seen[result_check], i]
            
        #     seen[value] = i
        # return []


        
       

