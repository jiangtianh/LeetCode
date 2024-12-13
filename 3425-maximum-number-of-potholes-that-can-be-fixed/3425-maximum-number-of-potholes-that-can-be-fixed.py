class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        road = road.split(".")
        road.sort(key=lambda x: -len(x))
        
        res = 0
        for r in road:
            if len(r) == 0 or budget == 0:
                break
            numToFix = min(budget-1, len(r))
            res += numToFix
            budget -= numToFix + 1

        return res