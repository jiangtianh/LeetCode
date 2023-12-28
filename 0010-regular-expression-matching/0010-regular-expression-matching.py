class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @cache
        def f(i, j):
            if j == len(p):
                return i == len(s)
            
    
            currentCharacterMatch = i < len(s) and (p[j] == s[i] or p[j] == ".")
            
        

            if j + 1 < len(p) and p[j+1] == "*":
                return f(i, j+2) or currentCharacterMatch and f(i+1, j) 
            else:
                return currentCharacterMatch and f(i+1, j+1)


        return f(0, 0)



    