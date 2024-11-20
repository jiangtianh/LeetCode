class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        allCount = Counter(s)
        aMax = allCount['a'] - k
        bMax = allCount['b'] - k
        cMax = allCount['c'] - k
        if aMax < 0 or bMax < 0 or cMax < 0:
            return -1

        d = collections.defaultdict(int)
        l = 0
        res = 0
        for r, c in enumerate(s):
            d[c] += 1
            while d['a'] > aMax or d['b'] > bMax or d['c'] > cMax:
                d[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return len(s) - res