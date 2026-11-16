class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        [-4, -1, -1, -1, -1, 0, 1, 2, 3, 5]

        for n in range(len(nums) - 2):
            if n > 0 and nums[n] == nums[n - 1]:
                continue
            left, right = n + 1, len(nums) - 1 
            
            while left < right:
                target = (nums[left] + nums[right]) + nums[n]
                if target == 0:
                    results.append([nums[n], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left -1]:
                        left += 1
                    while left < right and nums[right] == nums[right  + 1]:
                        right -= 1

                elif nums[left] + nums[right] > - nums[n]:
                    right -= 1
                else:
                    left += 1

        return results


        
            