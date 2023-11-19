# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def f(node, dir, cur):
            if not node:
                return 
            
            self.res = max(self.res, cur)

            if dir == 'left':
                f(node.right, 'right', cur + 1)
                f(node.left, 'left', 1)
            else:
                f(node.left, 'left', cur + 1)
                f(node.right, 'right', 1)
        
        f(root, 'left', 0)
        f(root, 'right', 0)
        

        
        

        return self.res

        
        
























        