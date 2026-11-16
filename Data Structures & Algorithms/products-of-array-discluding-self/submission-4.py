class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        [1, 2, 4, 6]

        [0, 1, 2, 3]

        [1, 1, 2, 8]

        [48, 24, 6, 1]

        a1 = [1] * len(nums)
        a2 = [1] * len(nums)
        result = []

        for n in range(len(nums)):
            if n > 0:
                a1[n] = a1[n-1]*nums[n-1]
        
        for n in range(len(nums) -1, -1, -1):
            if n < len(nums) -1:
                a2[n] = a2[n+1]*nums[n+1]
        
        for i in range(len(nums)):
            result.append(a1[i]*a2[i])

        return result
            




                
        

       
       
        
        