class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        def check(k):
            res = 0
            for pile in piles:
                res += math.ceil(pile / k)
            return res <= h

        res = r
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                res = mid
                r = mid - 1
            else: 
                l = mid + 1
        
        return res