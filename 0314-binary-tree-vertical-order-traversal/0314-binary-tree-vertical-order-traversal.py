# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        li = collections.defaultdict(list)
        q = collections.deque()
        q.append([root, 0])
        while q:
            for _ in range(len(q)):
                node, m = q.popleft()
              
                li[m].append(node.val)
                if node.left:
                    q.append([node.left, m-1])
                if node.right:
                    q.append([node.right, m+1])


        return [li[i] for i in sorted(li.keys())]