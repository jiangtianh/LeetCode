# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def f(node, largest):
            if not node:
                return 
            
            if node.val >= largest:
                self.res += 1
                largest = node.val
                
            f(node.left, largest)
            f(node.right, largest)
            
        f(root, -math.inf)
        return self.res