class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def f(i):
            if i >= len(cost):
                return 0
            
            return min(f(i + 1), f(i + 2)) + cost[i]
        
        return min(f(0), f(1))