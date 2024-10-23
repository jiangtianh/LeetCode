# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        q = collections.deque()
        q.append([root, None])

        while q:
            d = collections.defaultdict(int)
            total = 0
            for node, parent in q:
                d[parent] += node.val
                total += node.val
            
            for _ in range(len(q)):
                node, parent = q.popleft()
                node.val = total - d[parent]

                if node.left:
                    q.append([node.left, node])
                if node.right:
                    q.append([node.right, node])
        
        return root
        