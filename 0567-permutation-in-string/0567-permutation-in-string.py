class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        counter = collections.Counter(s1)
        have = {}
        
        for i in range(len(s1)):
            have[s2[i]] = have.get(s2[i], 0) + 1
    
        l = 0
        for i in range(len(s1), len(s2)):
            if have == counter:
                return True
            have[s2[i]] = have.get(s2[i], 0) + 1
            
            have[s2[l]] -= 1
            if have[s2[l]] == 0:
                have.pop(s2[l])
            l += 1
        
        return have == counter
            
        
        
        
        