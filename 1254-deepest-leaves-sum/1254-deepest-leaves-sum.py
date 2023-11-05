# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        def f(node):
            if not node.left and not node.right:
                return 1, node.val
            
            leftLevel, leftVal = 0, 0
            rightLevel, rightVal = 0, 0

            if node.left:
                leftLevel, leftVal = f(node.left)
            if node.right:
                rightLevel, rightVal = f(node.right)
            
            if leftLevel == rightLevel:
                return leftLevel + 1, leftVal + rightVal
            elif leftLevel > rightLevel:
                return leftLevel + 1, leftVal 
            else:
                return rightLevel + 1, rightVal

        level, val = f(root)
        return val