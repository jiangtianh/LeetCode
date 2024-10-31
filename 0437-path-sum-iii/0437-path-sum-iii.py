# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        prefix = collections.defaultdict(int)
        prefix[0] = 1
        self.res = 0

        def f(node, total):
            if not node:
                return 
            total += node.val
            
            self.res += prefix[total - targetSum]
            prefix[total] += 1
            f(node.left, total)
            f(node.right, total)
            prefix[total] -= 1

            
            
        f(root, 0)
        return self.res
