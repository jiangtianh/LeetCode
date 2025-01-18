class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        res = ""
        tCounter = collections.Counter(t)
        need = n
        l = 0

        for r, c in enumerate(s):
            if c not in tCounter:
                continue
            tCounter[c] -= 1

            if tCounter[c] >= 0:
                need -= 1
            
            while need == 0:
                if res == "" or r - l + 1 < len(res):
                    res = s[l:r+1]
                lc = s[l]
                l += 1
                if lc not in tCounter:
                    continue
                
                tCounter[lc] += 1
                if tCounter[lc] > 0:
                    need += 1
                
                
        return res