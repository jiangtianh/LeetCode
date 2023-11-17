class Solution:
    def decodeString(self, s: str) -> str:
        
        
        stack = []
        res = []
        
        def f(i):
            while i < len(s):
                count = ""
                while s[i].isnumeric():
                    count += s[i]
                    i += 1
                count = int(count)

                i += 1
                temp = ""
                while s[i] != "]":
                    if s[i].isnumeric():
                        res, i = f(i)
                        temp += res
                    else:
                        temp += s[i]
                    i += 1
                
                return temp * count, i
            
        result = ""
        i = 0
        while i < len(s):
            if s[i].isnumeric():
                res, i = f(i)
                result += res
            else:
                result += s[i]
            i += 1
        return result
            
            