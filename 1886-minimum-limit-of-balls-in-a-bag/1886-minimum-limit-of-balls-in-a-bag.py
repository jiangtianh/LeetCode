class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l = 1
        r = max(nums)
        res = r
        def canDivide(p):
            c = 0
            for n in nums:
                if n > p:
                    if n % p == 0:
                        c += n // p - 1
                    else:
                        c += n // p
                if c > maxOperations:
                    return False

            return c <= maxOperations

        
        while l <= r:
            pan = (l + r) // 2
            if canDivide(pan):
                res = min(res, pan)
                r = pan - 1
            else:
                l = pan + 1

        return res