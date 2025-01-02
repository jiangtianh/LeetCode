# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        li = collections.deque()

        def f(node):
            if not node:
                return 
            
            f(node.left)

            if len(li) < k:
                li.appendleft(node.val)
            else:
                if abs(node.val - target) <= abs(li[-1] - target):
                    li.pop()
                    li.appendleft(node.val)
            f(node.right)
        f(root)
        return list(li)