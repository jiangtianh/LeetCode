class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        res = 0

        def f(i):
            current = int(s[i])
            if current > k:
                return -1
            i += 1

            while i < len(s) and current * 10 + int(s[i]) <= k:
                current = current * 10 + int(s[i])
                i += 1
            return i

        i = 0
        while i < len(s):
            newIdx = f(i)
            if newIdx == -1:
                return -1
            i = newIdx
            res += 1
        return res
        