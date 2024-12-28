# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None
        
        def f(node):
            if not node or self.res is not None:
                return False
            left = f(node.left)
            mid = node is p or node is q
            right = f(node.right)
            if left and mid or left and right or right and mid:
                self.res = node
                return False
            return left or mid or right
        f(root)
        return self.res
