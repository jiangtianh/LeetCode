# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return ""
        
        self.res = []
        
        def f(node, temp):
            if not node.left and not node.right:
                self.res.append(temp)
                return 
            
            if node.left:
                f(node.left, temp + "->" + str(node.left.val))
            if node.right:
                f(node.right, temp + "->" + str(node.right.val))
            
            
            
        
        f(root, str(root.val))
        return self.res