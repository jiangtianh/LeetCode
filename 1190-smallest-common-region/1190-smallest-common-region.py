class TreeNode:
    def __init__(self, region):
        self.region = region
        self.neighbor = []
        self.parent = None

class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        d = {}

        for li in regions:
            if li[0] not in d:
                d[li[0]] = TreeNode(li[0])
            node = d[li[0]]

            for i in range(1, len(li)):
                if li[i] not in d:
                    d[li[i]] = TreeNode(li[i])
                d[li[i]].parent = node
                node.neighbor.append(d[li[i]])
        
        temp = d[regions[0][0]]
        while temp.parent != None:
            temp = temp.parent
        
        self.res = None
        def f(node):
            if self.res:
                return 0
            if node.region == region1 or node.region == region2:
                res = 1
            else:
                res = 0
            
            for nei in node.neighbor:
                res += f(nei)
            
            if res == 2:
                self.res = node.region
            if res:
                return 1
            else:
                return 0
        f(temp)
        return self.res