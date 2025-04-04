# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.deepest = 0
        self.res = None

        def f(node, depth):
            if not node:
                return depth - 1
            
            left = f(node.left, depth + 1)
            right = f(node.right, depth + 1)
            if left == right and left >= self.deepest:
                self.deepest = left
                self.res = node
            return max(left, right)
        
        f(root, 0)
        return self.res

            