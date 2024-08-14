# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def isLeaf(node):
            return not node.left and not node.right 
        
        def findDeepest(node, depth):
            if isLeaf(node):
                return depth
            left = findDeepest(node.left, depth + 1) if node.left else 0
            right = findDeepest(node.right, depth + 1) if node.right else 0
            return max(left, right)

        self.deepest = findDeepest(root, 0)
        self.res = root

        def f(node, depth):
            if not node:
                return False
            if depth == self.deepest:
                self.res = node
                return True 
            left = f(node.left, depth+1)
            right = f(node.right, depth+1)

            if left and right:
                self.res = node
            return left or right 

        f(root, 0)
        return self.res
            