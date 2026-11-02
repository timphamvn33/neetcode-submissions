# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # using depth first search or recursive
        # if not root :
        #     return 0
        
        # resultleft = 1 + self.maxDepth(root.left)
        # resultright = 1 + self.maxDepth(root.right)

        # maxresult = max(resultleft, resultright)
        # return maxresult

        # breadth first search iterative way
        
        if not root:
            return 0
        queue = deque([root])
        dept = 0
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            dept += 1
        return dept

                
            


