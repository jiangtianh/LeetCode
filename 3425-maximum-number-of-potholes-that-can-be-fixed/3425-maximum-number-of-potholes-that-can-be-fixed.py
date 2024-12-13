class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        li = []
        i = 0
        
        road = road.split(".")
        road.sort(key=lambda x: -len(x))
        
        res = 0
        for i, r in enumerate(road):
            if len(r) == 0:
                continue
            numToFix = min(budget-1, len(r))
            res += numToFix
            budget -= numToFix + 1

            if budget == 0:
                break

        return res