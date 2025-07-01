# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def f(node):
            if not node:
                return 0, math.inf, -math.inf
            leftSize, leftMin, leftMax = f(node.left)
            rightSize, rightMin, rightMax = f(node.right)
            if leftSize == -1 or rightSize == -1:
                return -1, 0, 0
            if leftMax >= node.val or node.val >= rightMin:
                return -1, 0, 0 
            else:
                self.res = max(self.res, leftSize + rightSize + 1)
                return leftSize + rightSize + 1, min(leftMin, node.val), max(rightMax, node.val)
            
                

        f(root)
        return self.res