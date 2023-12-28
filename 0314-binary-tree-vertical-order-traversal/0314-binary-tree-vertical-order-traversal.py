# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = collections.defaultdict(list)
    
        if not root:
            return []
        
        q = collections.deque()
        
        q.append((root, 0))
        
        while q:
            curr, position = q.popleft()
            self.res[position].append(curr.val)
            
            if curr.left:
                q.append((curr.left, position-1))
            if curr.right:
                q.append((curr.right, position+1))
        

        
        res = []
        for key in sorted(self.res.keys()):
            res.append(self.res[key])
        
        return res
        
        
        
        
        