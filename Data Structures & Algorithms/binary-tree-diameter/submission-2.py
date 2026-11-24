# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_h = 0
        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            h_l= dfs(root.left) 
            h_r= dfs(root.right)

            self.max_h = max(self.max_h, (h_l + h_r))

            return max(h_l, h_r) + 1
        dfs(root)
        return self.max_h




            