# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        results = []
        def bst_array(root):
            
            if not root:
                return
            bst_array(root.left)
            results.append(root.val)
            bst_array(root.right)
        bst_array(root)
        return results[k-1]
            

