# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.diff = 0
        
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)
            self.diff = max(self.diff, abs(left_height - right_height))
            return max(left_height, right_height) + 1
        dfs(root)
        return self.diff <= 1


        