class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # using binary search. using the middle as a pointer if the target < value at middle then move left += 1, if target > value at middle then move the right pointer += 1
        left, right = 0, len(nums) -1

        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right -= 1
            else:
                left += 1
        return -1
