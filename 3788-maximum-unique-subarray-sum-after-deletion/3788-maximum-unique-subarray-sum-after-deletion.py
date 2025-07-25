class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s = set()
        res = 0
        maximum = -math.inf
        for n in nums:
            if n < 0 or n in s:
                maximum = max(maximum, n)
                continue
            s.add(n)
            res += n
        if len(s) == 0:
            return maximum
        return res