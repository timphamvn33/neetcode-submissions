class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = defaultdict(int)
        for i, n in enumerate(nums):
            diff = target - n

            if diff in mp:
                return [mp[diff], i]
            mp[n]=i
        

        
             


        




















        # seen = {}

        # for i, value in enumerate(nums):
        #     result_check = target - value
        #     if result_check in seen:
        #         return [seen[result_check], i]
            
        #     seen[value] = i
        # return []


        
       

