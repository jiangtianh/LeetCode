class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        def canLoad(maxWeight):
            res = 0
            cur = 0
            for w in weights:
                if cur + w > maxWeight:
                    res += 1
                    cur = w
                else:
                    cur += w
            return res + 1
        res = math.inf
        while l <= r:
            m = (l + r) // 2
            dayTake = canLoad(m)
            if dayTake <= days:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1

        return res
