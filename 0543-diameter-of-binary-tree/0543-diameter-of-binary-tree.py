# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def f(node):
            if not node:
                return 0 
            left = 0
            right = 0
            
            if node.left:
                left = f(node.left) + 1    

            if node.right:
                right = f(node.right) + 1


            self.res = max(self.res, left + right)

            return max(left, right)

        f(root)
        return self.res    
