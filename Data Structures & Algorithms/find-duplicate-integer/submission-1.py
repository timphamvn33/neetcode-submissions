class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # using the floyd cycle detection slow fast to solve the problem
        slow = nums[0]
        fast = nums[0]

        # find the intersection between slow and fast where fast = slow
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        # get start find the duplicate keep the fast and move slow back to o
        slow = nums[0]
        while slow!=fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow