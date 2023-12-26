class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        def checkV6(li):
            if len(li) != 8:
                return False 
            for s in li:
                if len(s) > 4 or len(s) < 1:
                    return False 
                for c in s:
                    if not c.isnumeric():
                        if not((ord("A") <= ord(c) <= ord("F")) or (ord("a") <= ord(c) <= ord("f"))):
                            return False 
            return True 
            
        def checkV4(li):
            if len(li) != 4:
                return False 
            else:
                for s in li:
                    if len(s) > 1:
                        if s[0] == "0":
                            return False 
                    if not s.isnumeric() or int(s) < 0 or int(s) > 255:
                        return False 
                return True 
        
        def read(s):
            temp = ""
            res = []
            isV4, isV6 = False, False 
            
            for c in s:
                if c == "." or c == ":":
                    if c == ".":
                        isV4 = True 
                    else:
                        isV6 = True 
                    res.append(temp)
                    temp = ""
                else:
                    temp += c
            res.append(temp)
            return res, isV4, isV6
        
        
        li, isV4, isV6 = read(queryIP)
        
        
        if isV4 and isV6:
            return "Neither"  
        elif isV4:
            if checkV4(li):
                return "IPv4"
            return "Neither" 
        elif isV6:
            if checkV6(li):
                return "IPv6"
            return "Neither" 
        else:
            return "Neither" 
                    
        
        
        
        
        
    