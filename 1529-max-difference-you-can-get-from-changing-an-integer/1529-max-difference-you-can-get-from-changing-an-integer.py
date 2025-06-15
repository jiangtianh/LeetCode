class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        idx = 0
        while idx < len(s) and s[idx] == "9":
            idx += 1
        if idx < len(s):
            c = s[idx]
            a = int(s.replace(c, "9"))
        else:
            a = num
        
        idx = 0
        while idx < len(s) and (s[idx] == "1" or s[idx] == "0"):
            idx += 1
        if idx < len(s):
            c = s[idx]
            if idx == 0:
                b = int(s.replace(c, "1"))
            else:
                b = int(s.replace(c, "0"))
        else:
            b = num
        print(a) 
        print(b)
        return a - b