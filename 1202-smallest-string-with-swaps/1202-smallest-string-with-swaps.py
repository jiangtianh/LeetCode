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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UF(len(s))
        
        for i, j in pairs:
            uf.join(i, j)
        
        d = defaultdict(list)
        for i in range(len(s)):
            d[uf.find(i)].append(i)    
        
        li = list(s)
            
        for root in d:
            idxList = []
            charList = []
            for idx in d[root]:
                idxList.append(idx)
                charList.append(s[idx])
            idxList.sort() 
            charList.sort() 
            
            for i in range(len(idxList)):
                li[idxList[i]] = charList[i]
        
        return "".join(li)





