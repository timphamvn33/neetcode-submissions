class Solution:
    def maxArea(self, heights: List[int]) -> int:
        len_h = len(heights)
        mw = 0
        left, right = 0, len_h -1

        while left < right:
            curr_h = min(heights[left], heights[right])
            cur_mw = curr_h*(right-left)
            mw = max(mw, cur_mw)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return mw
            
        
            



    





















        # n = len(heights)
        # left, right = 0, n - 1
        # max_area = 0

        # while left < right:
        #     width = right - left
        #     min_height = min(heights[left], heights[right] )
        #     max_area = max(max_area, width * min_height)

        #     # always move the pointer toward the higher height
        #     if heights[left] < heights[right]:
        #         left += 1
        #     else:
        #         right -= 1
        # return max_area
        