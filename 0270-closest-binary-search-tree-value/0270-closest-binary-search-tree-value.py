# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        self.res = root.val

        def f(node):
            if not node:
                return 

            if abs(node.val - target) < abs(self.res - target):
                self.res = node.val
            elif abs(node.val - target) == abs(self.res - target):
                self.res = min(node.val, self.res)
            
            if node.val < target:
                f(node.right)
            else:
                f(node.left)

        f(root)
        return self.res