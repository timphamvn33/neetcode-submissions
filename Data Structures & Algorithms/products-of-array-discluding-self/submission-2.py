class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        [1, 2, 4, 6]
        [1, 1, 2, 8]
        [48, 24, 6, 1]

        [48, 24, 12, 8]

        pre = [1]*len(nums)
        suf = [1]*len(nums)
        result = []

        for n in range(len(nums)):
            if n != 0:
                pre[n] = pre[n-1] * nums[n-1]
        for n in range(len(nums) -1, -1, -1):
            if n != len(nums) -1:
                suf[n] = suf[n+1] * nums[n+1]
        
        for i in range(len(nums)):
            result.append(pre[i] * suf[i])
        return result
                
        

       
       
        
        