class Solution:
    def maxRepOpt1(self, text: str) -> int:
        
        def f(c):
            res = 0
            lcounter = 0
            rcounter = text.count(c)
            
            r = 0
            l = 0
            otherChar = 0
            while r < len(text):
                char = text[r]
                if char == c:
                    rcounter -= 1
                else:
                    otherChar += 1
                
                if otherChar == 0:
                    res = max(res, r - l + 1)
                    r += 1
                else:
                    while otherChar > 1:
                        lchar = text[l]
                        if lchar == c:
                            lcounter += 1
                        else:
                            otherChar -= 1
                        l += 1
                
                    if (l > 0 and lcounter > 0) or (r < len(text) - 1 and rcounter > 0):
                        res = max(res, r - l + 1)
                    r += 1
            return res
        res = 0
        for i in range(26):
            c = chr(ord('a') + i)
            res = max(res, f(c))


        return res