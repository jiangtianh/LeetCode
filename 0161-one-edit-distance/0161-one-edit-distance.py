class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            edit = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    edit += 1
            return edit == 1
        elif abs(len(s) - len(t)) == 1:
            i, j, edit = 0, 0, 0
            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    i += 1
                    j += 1
                else:
                    if len(s) > len(t):
                        i += 1
                    else:
                        j += 1
                    edit += 1
            while i < len(s):
                i += 1
                edit += 1
            while j < len(t):
                j += 1
                edit += 1
            return edit == 1

        else:
            return False