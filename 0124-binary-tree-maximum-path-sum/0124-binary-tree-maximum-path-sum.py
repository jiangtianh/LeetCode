# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -math.inf

        def f(node):
            if not node:
                return 0 
            
            left = f(node.left)
            if left < 0:
                left = 0
            right = f(node.right)
            if right < 0:
                right = 0
            self.res = max(self.res, node.val + left + right)

            
            return max(left, right) + node.val

        f(root)
        return self.res



