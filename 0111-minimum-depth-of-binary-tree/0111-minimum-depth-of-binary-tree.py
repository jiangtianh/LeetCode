# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def f(node):
            if not node:
                return math.inf
            if not node.left and not node.right:
                return 1
            
            return min(f(node.left), f(node.right)) + 1

        if not root:
            return 0
        return f(root)