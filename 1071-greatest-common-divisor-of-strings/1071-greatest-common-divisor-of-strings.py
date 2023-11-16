class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if len(str1) > len(str2):
            shorter = str2
            longer = str1
        else:
            shorter = str1
            longer = str2
            
        i = len(shorter)
        
        while i > 0:
            divisor = shorter[0:i]
            
            if len(str1) % len(divisor) != 0:
                i -=1
                continue 
            
            shorter_verified = True
            for j in range(i, len(shorter), i):
                if shorter[j:j+i] != divisor:
                    shorter_verified = False 
                    break
                    
            if not shorter_verified:
                i -= 1
                continue 
            
            longer_verified = True
            for j in range(0, len(longer), i):
                if longer[j:j+i] != divisor:
                    longer_verified = False
                    break
            
            if shorter_verified and longer_verified:
                return divisor
            
            i -= 1
                
                
                
        return ""
            
        
        
        