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
                self.res.append("".join(temp))
                return 
            
            if node.left:
                temp.append("->" + str(node.left.val))
                f(node.left, temp)
                temp.pop()
            if node.right:
                temp.append("->" + str(node.right.val))
                f(node.right, temp)
                temp.pop()
            
            
        
        f(root, [str(root.val)])
        return self.res