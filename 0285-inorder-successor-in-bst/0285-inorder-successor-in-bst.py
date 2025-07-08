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
                return 
            f(node.left)
            f(node.right)
            if node.val > p.val:
                if not self.res or self.res.val > node.val:
                    self.res = node
                
        f(root)
        return self.res