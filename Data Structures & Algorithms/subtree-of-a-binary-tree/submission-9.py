# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        if self.isMatch(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def isMatch(self, root1, root2):
        if not root1 and not root2:
            return True
        elif not root1 or not root2:
            return False
        left = self.isMatch(root1.left, root2.left)
        right = self.isMatch(root1.right, root2.right)

        val_same = root1.val == root2.val
        return val_same and left and right