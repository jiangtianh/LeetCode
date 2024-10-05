class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0   
        d = collections.Counter(s1)        

        need = len(s1)

        for r in range(len(s2)):
            c = s2[r]
            if c in d and d[c] > 0:
                need -= 1
                d[c] -= 1
            elif c in d:
                while s2[l] != c:
                    if s2[l] in d:
                        d[s2[l]] += 1
                        need += 1
                    l += 1
                l += 1
            else:
                while l <= r:
                    lc = s2[l]
                    if lc in d:
                        d[lc] += 1
                        need += 1
                    l += 1
                    
            if need == 0:
                return True 

        return False