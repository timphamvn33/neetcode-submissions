# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter of a node = edege of node.left + edege of node.right
        self.max_path = 0
        def dfs(root: optional[TreeNode]) -> int:
            if not root:
                return 0
            edge_left = dfs(root.left)
            edge_right = dfs(root.right)

            self.max_path = max(self.max_path, (edge_left + edge_right))

            return max(edge_left, edge_right) + 1
        dfs(root)
        return self.max_path


            