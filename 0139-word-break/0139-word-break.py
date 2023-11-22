class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        @cache
        def f(i):
            
            if i == len(s):
                return True 
            
            res = False
            for j in range(i, len(s)):
                if s[i:j + 1] in wordDict:
                    res = res or f(j + 1)
            return res
        
        return f(0)
            
        
        