class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using hasmash to solve this problem.
        # if the target minus to one of the element and that value not seen in that hash map then add that (value, index) into the hashmap else return that element index and the element found in set

        seen = {}

        for i, value in enumerate(nums):
            result_check = target - value
            if result_check in seen:
                return [seen[result_check], i]
            
            seen[value] = i
        return []


        
       

