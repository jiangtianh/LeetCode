class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        lc = 0
        res = []
        for c in s:
            if c == "(":
                lc += 1
            elif c == ")":
                if lc == 0:
                    continue
                lc -= 1
            res.append(c)
        idx = len(res) - 1
        while lc > 0:
            if res[idx] == "(":
                res.pop(idx)
                lc -= 1
            idx -= 1
        
        return ''.join(res)


