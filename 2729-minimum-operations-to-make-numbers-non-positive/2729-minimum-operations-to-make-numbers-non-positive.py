class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        l = 0
        r = math.ceil(max(nums) / y)

        def check(steps):
            xsteps = steps
            base = y * steps

            for n in nums:
                left = n - base
                if left > 0:
                    xsteps -= math.ceil(left / (x - y))
                    if xsteps < 0:
                        return False
            return True
        
        while l <= r:
            m = (l + r) // 2
            if check(m):
                r = m - 1
            else:
                l = m + 1
        return l
        