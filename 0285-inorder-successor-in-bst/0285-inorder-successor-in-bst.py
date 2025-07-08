# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        self.res = None

        def f(node):
            if not node:
                return None
            if node.val > p.val:
                if not self.res or self.res.val > node.val:
                    self.res = node
            
            if node.val > p.val:
                f(node.left)
            else:
                f(node.right)
            
            
                
        f(root)
        return self.res