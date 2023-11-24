class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def check(k):
            hour = 0
            for banana in piles:
                hour += math.ceil(banana / k)
                if hour > h:
                    return False 
            return hour <= h

        l = 1
        r = max(piles)

        while l <= r:
            m = (l + r) // 2
            res = check(m)

            if res:
                r = m - 1
            else:
                l = m + 1
            
        return l

