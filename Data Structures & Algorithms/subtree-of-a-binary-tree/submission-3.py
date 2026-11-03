# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # recursive

        if not subRoot:
            return True
        if not root:
            return False
        if self.isMatchTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isMatchTree(self, q: Optional[TreeNode], p: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True
        if not q or not p or q.val != p.val:
            return False
        result = self.isMatchTree(q.left, p.left) and self.isMatchTree(q.right, p.right) 
        return result 
        # using the iterative way
