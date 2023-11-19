class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None 

class Solution:
    def pathSum(self, nums: List[int]) -> int:
        def getIdx(num):
            num = str(num)
            level = num[0]
            order = num[1]
            
            return 2 ** (int(level) - 1) + int(order) - 1
    
        self.li = [math.inf] * 16
        
        for num in nums:
            self.li[getIdx(num)] = int(str(num)[2])
         
        def build(i):
            if i >= 16 or self.li[i] == math.inf:
                return None 
            node = TreeNode(self.li[i])     
            node.left = build(i * 2)
            node.right = build(i * 2 + 1)
            return node 
        
        root = build(1)
        
        self.res = 0
        def f(node, cur):
            if not node:
                return 
            
            if not node.left and not node.right:
                self.res += cur + node.val
                return 
            else:
                f(node.left, cur + node.val)
                f(node.right, cur + node.val)
        
        f(root, 0)
        return self.res
            
            
            
            
            
            
            
        
            
            
            
            
            
            
            
        