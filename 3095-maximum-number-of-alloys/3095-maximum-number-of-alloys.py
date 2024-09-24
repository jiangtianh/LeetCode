class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:

        def calculateCost(numOfAlloy, machineIdx):
            res = 0
            for i in range(n):
                totalMetal = composition[machineIdx][i] * numOfAlloy
                metalNeeded = totalMetal - stock[i]
                if metalNeeded > 0:
                    tempCost = (cost[i] * metalNeeded)
                    res += tempCost
            return res
        
        res = 0
        for machineIdx in range(k):
            l = 0
            r = 2 * 10 ** 9
            while l <= r:
                m = (l + r) // 2
                costs = calculateCost(m, machineIdx)
                if costs > budget:
                    r = m - 1
                else:
                    l = m + 1
            res = max(res, r)
        return res


        # n types of metal available 
        # k machines 

        # ith machine to create jth alloy, need composition[i][j]

        # initially have stock[j] units of metal type j 

        # purchasing one unit of metal type j costs cost[j]