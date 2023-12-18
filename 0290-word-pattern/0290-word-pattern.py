class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patternToWord = {}
        wordToPattern = {}
        
        s = s.split(" ")
        if len(s) != len(pattern):
            return False
        for i in range(len(pattern)):
            p = pattern[i]
            w = s[i]
            
            if w not in wordToPattern and p not in patternToWord:
                patternToWord[p] = w
                wordToPattern[w] = p
        
            elif w in wordToPattern and p in patternToWord:
                if patternToWord[p] != w or wordToPattern[w] != p:
                    return False 
            else:
                return False 
        return True
                
                
                
        
        