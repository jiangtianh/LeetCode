class UF:
    def __init__(self, n):
        self.li = [i for i in range(n)]
        self.rank = [0] * n
        
    def find(self, i):
        if self.li[i] == i:
            return i 
        else:
            return self.find(self.li[i])
        
    def join(self, i, j):
        iRoot, jRoot = self.find(i), self.find(j)
        
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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UF(len(isConnected))
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    uf.join(i, j)
        s = set()       
        for i in range(len(isConnected)):
            s.add(uf.find(i))
        return len(s)
        
        
        
        