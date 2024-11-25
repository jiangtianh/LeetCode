class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        d = {}
        unique = set()

        def f(i, j):
            if i == len(pattern) and j == len(s):
                return True 
            if i == len(pattern) or j == len(s):
                return False 
            pat = pattern[i]
            if pat in d:
                idx = 0
                while idx < len(d[pat]) and j + idx < len(s):
                    if d[pat][idx] == s[j + idx]:
                        idx += 1
                    else:
                        return False
                if j + idx <= len(s):
                    return f(i+1, j + idx)
                else:
                    return False
            else:
                temps = []
                for idx in range(j, len(s)):
                    c = s[idx]
                    temps.append(c)
                    curString = "".join(temps)
                    d[pat] = curString
                    if curString in unique:
                        continue 
                    unique.add(curString)
                    
                    if f(i+1, idx + 1):
                        return True
                    unique.remove(curString)
                d.pop(pat)
                return False

        return f(0, 0)