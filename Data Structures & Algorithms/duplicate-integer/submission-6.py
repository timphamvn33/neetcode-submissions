class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ns = set()

        for num in nums:
            if num in ns:
                return True
            ns.add(num)
        return False