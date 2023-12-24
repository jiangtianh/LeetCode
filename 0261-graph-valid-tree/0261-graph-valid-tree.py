class UnionFind:
    def __init__(self, n):
        self.li = [i for i in range(n)]
        self.rank = [0] * n

        
    def find(self, i):
        if self.li[i] == i:
            return i 
        else:
            return self.find(self.li[i])
        
    def join(self, i, j):
        iRoot = self.find(i)
        jRoot = self.find(j)
        
        if iRoot == jRoot:
            return False 
        else:
            if self.rank[iRoot] > self.rank[jRoot]:
                self.li[jRoot] = iRoot
                self.rank[iRoot] += 1
            else:
                self.li[iRoot] = jRoot
                self.rank[jRoot] += 1
            return True 
        
        
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1:
            return False
        
        
        unionFind = UnionFind(n)
        
        for i, j in edges:
            if not unionFind.join(i, j):
                return False 
    
        return True
        
        
        

        
        

    
        
        
        
        