# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def f(node):

            if not node.left and not node.right:
                return node.val, node.val
            cur = node.val
            leftMax, leftMin, rightMax, rightMin = cur, cur, cur, cur 
            if node.left:
                leftMax, leftMin = f(node.left)
            if node.right:
                rightMax, rightMin = f(node.right)
            
            self.res = max(self.res, abs(cur - min(leftMin, rightMin)))
            self.res = max(self.res, abs(cur - max(leftMax, rightMax)))

            return max(cur, leftMax, rightMax), min(cur, rightMin, leftMin)

        f(root)
        return self.res