# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def f(node, temp):
            if not node.left and not node.right:
                self.res += (int(temp + str(node.val)))
                return 
            if node.left:
                f(node.left, temp + str(node.val))
            if node.right:
                f(node.right, temp + str(node.val))
        
        f(root, "")
        return self.res
                
                
                
                
                