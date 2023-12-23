class UnionFind:
    def __init__(self, size):
        self.li = [i for i in range(size)]
        self.rank = [0] * size
        
    def find(self, node):
        if self.li[node] == node:
            return node
        else:
            return self.find(self.li[node])
    def join(self, i, j):
        iRoot = self.find(i)
        jRoot = self.find(j)
        if iRoot == jRoot:
            return False 
        if self.rank[iRoot] > self.rank[jRoot]:
            self.li[jRoot] = iRoot
            self.rank[iRoot] += 1
        else:
            self.li[iRoot] = jRoot
            self.rank[jRoot] += 1
        return True 
    
    
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        def getDistance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])  
        
        li = []
        
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                heapq.heappush(li, (getDistance(points[i], points[j]), i, j))
        
        edges = 0
        totalCost = 0 
        unionfind = UnionFind(len(points))
        
        while edges < len(points) - 1:
            cost, i, j = heapq.heappop(li)
            if unionfind.join(i, j):
                totalCost += cost
                edges += 1
        
        return totalCost
        

    
        
        
        
        
        
        