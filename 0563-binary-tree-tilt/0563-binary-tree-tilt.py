# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def f(node):
            if not node:
                return 0

            lSum = f(node.left) 
            rSum = f(node.right)
            self.res += abs(lSum - rSum)
            return rSum + lSum + node.val
        
        f(root)
        return self.res