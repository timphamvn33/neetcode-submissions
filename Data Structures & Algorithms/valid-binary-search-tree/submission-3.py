# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        results = []
        def is_asc_list(root):
            if not root:
                return
            is_asc_list(root.left)
            results.append(root.val)
            is_asc_list(root.right)
        is_asc_list(root)

        for i in range(1, len(results), 1):
            if results[i] <= results[i-1]:
                return False
        return True

            