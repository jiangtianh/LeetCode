class DisjointSet:
    def __init__(self, n):
        self.li = [i for i in range(n + 1)]
        self.rank = [0 for _ in range(n + 1)]
    def find(self, x):
        if self.li[x] == x:
            return x
        res = self.find(self.li[x])
        self.li[x] = res
        return res
    def join(self, x, y):
        xRoot, yRoot = self.find(x), self.find(y)
        if xRoot == yRoot:
            return False
        if self.rank[xRoot] > self.rank[yRoot]:
            self.li[yRoot] = xRoot
        elif self.rank[xRoot] < self.rank[yRoot]:
            self.li[xRoot] = yRoot
        else:
            self.li[yRoot] = xRoot
            self.rank[xRoot] += 1
        return True 
    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        ds = DisjointSet(n)
        for x, y in edges:
            if not ds.join(x, y):
                return [x, y]
