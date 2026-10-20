class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # using binary search by move from left = 0 to right = m*n -1 instead of flattening the array. reduce the time complexity
        # 
        row = len(matrix)
        col = len(matrix[0])
        left, right = 0, row*col -1

        while left <= right:
            mid = left + (right - left)//2
            mid_col = mid % col
            mid_row = mid // col
            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] > target:
                right -= 1
            else:
                left += 1
        return False