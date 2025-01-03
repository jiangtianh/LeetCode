# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        res = [root.val]
        def getLeaves(node):
            if not node:
                return 
            if not node.left and not node.right:
                res.append(node.val)
            getLeaves(node.left)
            getLeaves(node.right)  
        
        def getLeft(node):
            if not node:
                return
            if node.left or node.right:
                res.append(node.val)
            if node.left:
                getLeft(node.left)
            else:
                getLeft(node.right)

        def getRight(node):
            if not node:
                return
            if node.right:
                getRight(node.right)
            else:
                getRight(node.left)
            if node.left or node.right:
                res.append(node.val)        

        getLeft(root.left)
        if root.left or root.right:
            getLeaves(root)
        getRight(root.right)


        return res