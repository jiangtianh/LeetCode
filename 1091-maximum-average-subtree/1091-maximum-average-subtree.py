# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.res = -math.inf
        def f(node):
            if not node:
                return 0, 0
            lsum, l = f(node.left)
            rsum, r = f(node.right)
            total, count = node.val + lsum + rsum, l + r + 1
            self.res = max(self.res, total / count)
            return total, count
        f(root)
        return self.res