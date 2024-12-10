class Solution:
    def maximumLength(self, s: str) -> int:
        d = collections.defaultdict(int)

        tempD = {}
        l = 0

        for r, c in enumerate(s):
            tempD[c] = tempD.get(c, 0) + 1
            
            while len(tempD) > 1:
                lc = s[l]
                tempD[lc] -= 1
                if tempD[lc] == 0:
                    tempD.pop(lc)
                l += 1
                
            for i in range(1, r - l + 1 + 1):
                d[c * i] += 1

        times = 0
        res = 0
        for subStr in d:
            if d[subStr] >= 3 and d[subStr] >= times:
                res = max(res, len(subStr))
        
        if res == 0:
            return -1
        return res