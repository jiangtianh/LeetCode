class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        
        @cache
        def f(i):
            if i == len(s):
                return True 
            elif i > len(s):
                return False 
            res = False 
            for word in wordDict:
                if s[i:i+len(word)] == word:
                    res = res or f(i + len(word))
                    if res:
                        break
            return res
        
        return f(0)