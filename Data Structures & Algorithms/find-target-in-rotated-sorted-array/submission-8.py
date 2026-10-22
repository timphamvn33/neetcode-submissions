class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # naive solutio is iterate the the nums and return the index if we find the target but running time will be O(n) using binary will speed up the running to O(logn)
        # using binary left = 0 and  right = len(nums) - 1
        
        left, right = 0, len(nums) -1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target: 
                return mid
            # if nums[mid] > target
            if nums[left] <= nums[mid]:
                # half left sorted
                if nums[left] <= target < nums[mid]:
                    # move right
                    right = mid -1
                # half right not sorted
                else:
                    left = mid + 1
            else:
                # half right sorted
                if nums[right] >= target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1