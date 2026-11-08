class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        [-4, -1, -1, -1, 2, 2]
        result = []
        nums.sort()
        for n in range(len(nums)):
            
            if n > 0 and nums[n] == nums[n-1]:
                continue
            left, right = n + 1, len(nums) -1
            while left< right:
                total = nums[n] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[n],nums[left], nums[right]] )
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left -1]:
                        left += 1
                    while left < right and nums[right] == nums[right +1]:
                        right -= 1
                    
        return result
