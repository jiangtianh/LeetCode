class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a = str(bin(a))[2:]
        b = str(bin(b))[2:]
        c = str(bin(c))[2:]
        
        maxLength = max(len(a), len(b), len(c))
        
        while len(a) != maxLength:
            a = "0" + a
        while len(b) != maxLength:
            b = "0" + b
        while len(c) != maxLength:
            c = "0" + c
        
        
        print(a)
        print(b)
        print(c)
        
        res = 0
        for i in range(len(c)):
            cbit = c[i]
            abit = a[i]
            bbit = b[i]
            if cbit == "0":
                if abit == "1" and bbit == "1":
                    res += 2
                elif abit == "1" or bbit == "1":
                    res += 1
            elif cbit == "1":
                if abit == "0" and bbit == "0":
                    res += 1
                    
        return res
            
            
            
            