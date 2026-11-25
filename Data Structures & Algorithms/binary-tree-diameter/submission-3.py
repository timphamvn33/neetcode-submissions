# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_he = 0
        def dfs(root: Optional[TreeNode]):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            self.max_he = max(self.max_he, (left+right))

            return max(left, right) + 1
        dfs(root)
        return self.max_he