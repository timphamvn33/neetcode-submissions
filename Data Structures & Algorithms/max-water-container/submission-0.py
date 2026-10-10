class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = 0, n - 1
        max_area = 0

        while left < right:
            width = right - left
            min_height = min(heights[left], heights[right] )
            max_area = max(max_area, width * min_height)

            # always move the pointer toward the higher height
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area
        