# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.res = 1
        def f(node, prev, length):
            if not node:
                return 
            
            if node.val == prev + 1:
                self.res = max(self.res, length + 1)
            
                f(node.left, node.val, length + 1)
                f(node.right, node.val, length + 1)
            else:
                f(node.left, node.val, 1)
                f(node.right, node.val, 1)

            
        




        f(root, -1, 0) 
        return self.res