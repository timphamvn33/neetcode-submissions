class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create set row, column, and box
        # check if value in row or col or box then return false
        # if the val = . then continue
        # set the value to row, col, box to track the value

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                box_id = (row//3, col//3)

                if(val in rows[row] or 
                    val in cols[col] or 
                    val in boxes[box_id]):
                    return False

                rows[row].add(val)
                cols[col].add(val)
                boxes[box_id].add(val)
        return True