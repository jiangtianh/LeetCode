class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        
        l = 1
        r = max(ribbons)

        def check(n):
            res = 0
            for rib in ribbons:
                res += (rib // n)
            return res
        result = 0

        while l <= r:
            mid = (l + r) // 2
            temp = check(mid)
            if temp >= k:
                result = max(result, mid)
                l = mid + 1
            else:
                r = mid - 1
        
        return result