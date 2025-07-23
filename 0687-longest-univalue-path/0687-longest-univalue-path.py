# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.res = 0

        def f(node):
            if not node.left and not node.right:
                res = 1
            
            elif node.left and node.right:
                left = f(node.left)
                right = f(node.right)
                if node.val == node.left.val and node.val == node.right.val:
                    self.res = max(self.res, left + right + 1)
                    res = max(left, right) + 1
                elif node.val == node.left.val:
                    res = left + 1
                elif node.val == node.right.val:
                    res = right + 1
                else:
                    res = 1
                
            elif node.left:
                left = f(node.left)
                if node.val == node.left.val:
                    res = left + 1
                else:
                    res = 1

            elif node.right:
                right = f(node.right)
                if node.val == node.right.val:
                    res = right + 1
                else:
                    res = 1
            self.res = max(self.res, res)
            return res
            
        f(root)
        return self.res - 1