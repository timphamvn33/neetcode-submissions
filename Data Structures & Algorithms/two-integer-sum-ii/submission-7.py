class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) -1
        while left < right:
            tg = numbers[left] + numbers[right]

            if target == tg:
                return [left +1, right + 1]
            elif target > tg:
                left += 1
            else:
                right -= 1
        return []