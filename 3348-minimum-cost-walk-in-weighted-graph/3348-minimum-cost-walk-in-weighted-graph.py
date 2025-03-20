class DisjointSet:
    def __init__(self, n):
        self.li = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.cost = {}
    def find(self, x):
        if self.li[x] == x:
            return x
        res = self.find(self.li[x])
        self.li[x] = res
        return res

    def join(self, x, y, cost):
        xRoot, yRoot = self.find(x), self.find(y)
        if xRoot != yRoot:
            if self.rank[xRoot] > self.rank[yRoot]:
                self.li[yRoot] = xRoot
            elif self.rank[xRoot] < self.rank[yRoot]:
                self.li[xRoot] = yRoot
            else:
                self.li[yRoot] = xRoot
                self.rank[xRoot] += 1
        self.addCost(xRoot, yRoot, cost)


    def addCost(self, newRoot, oldRoot, edgeCost):
        newCost = None
        oldCost = self.cost.get(oldRoot, None)
        rootCost = self.cost.get(newRoot, None)

        if rootCost is None and oldCost is None:
            newCost = edgeCost
        elif rootCost is None:
            newCost = oldCost & edgeCost
        elif oldCost is None:
            newCost = rootCost & edgeCost
        else:
            newCost = rootCost & oldCost & edgeCost

        self.cost[newRoot] = newCost
        self.cost[oldRoot] = newCost



    def lookup(self, x, y):
        if self.find(x) != self.find(y):
            return -1
        return min(self.cost.get(self.find(x), math.inf), self.cost.get(self.find(y), math.inf))

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        ds = DisjointSet(n)

        for x, y, w in edges:
            ds.join(x, y, w)
        print(ds.cost)

        print(ds.li)

        res = []
        for x, y in query:
            res.append(ds.lookup(x, y))
        return res
