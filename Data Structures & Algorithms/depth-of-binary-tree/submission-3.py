# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recrusive depth first search
        if not root:
            return 0
        res_left = 1 + self.maxDepth(root.left)
        res_right = 1 + self.maxDepth(root.right)

        return max(res_left, res_right)

        #breath first search
        # if not root:
        #     return 0
        # queue = deque([root])
        # count = 0
        # while queue:
        #     for _ in range(len(queue)):
        #         curr = queue.popleft()
        #         if curr.left:
        #             queue.append(curr.left)
        #         if curr.right:
        #             queue.append(curr.right)
        #     count += 1
        # return count

