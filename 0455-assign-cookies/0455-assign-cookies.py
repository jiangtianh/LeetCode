class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort() 
        g.sort() 
        res = 0
        cookieIdx = childIdx = 0
        
        while cookieIdx < len(s) and childIdx < len(g):
            greed = g[childIdx]
            
            while cookieIdx < len(s) and s[cookieIdx] < greed:
                cookieIdx += 1
            
            if cookieIdx == len(s):
                break 
            else:
                res += 1
                cookieIdx += 1
            
            childIdx += 1
        
        return res
        
        