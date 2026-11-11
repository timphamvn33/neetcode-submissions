class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = []
        if not nums:
            return []

        for n in range(len(nums) -2):
            if n > 0 and nums[n] == nums[n-1]:
                continue
            left, right = n +1, len(nums) -1

            while left < right:
                tg = nums[left] + nums[right]
                target = -nums[n]
                if tg == target:
                    result.append([nums[n], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left +=1
                    while left < right and nums[right] == nums[right +1]:
                        right -= 1

                    
                elif tg > target:
                    right -= 1
                else:
                    left += 1
        return result


