class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = collections.Counter(word1)
        count2 = collections.Counter(word2)
        
        d1 = {}
        d2 = {}
        
        for key in count1:
            d1[count1[key]] = d1.get(count1[key], 0) + 1
            if key not in count2:
                return False 
        for key in count2:
            d2[count2[key]] = d2.get(count2[key], 0) + 1
            if key not in count1:
                return False
        
        return d1 == d2 