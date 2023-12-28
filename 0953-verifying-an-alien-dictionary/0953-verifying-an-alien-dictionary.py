class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {order[i]:i for i in range(len(order))}
        
        
        def compareWord(word1, word2):
            
            for i in range(min(len(word1), len(word2))):
                if d[word1[i]] < d[word2[i]]:
                    return True 
                elif d[word1[i]] > d[word2[i]]:
                    return False 
            if len(word1) == len(word2):
                return True
            return len(word1) < len(word2)
        
        
        for i in range(1, len(words)):
            if not compareWord(words[i-1], words[i]):
                return False 
            
        return True
        
        
            
            