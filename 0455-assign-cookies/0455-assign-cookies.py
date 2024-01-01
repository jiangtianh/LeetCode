class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort() 
        g.sort() 
        res = 0
        cookieIdx = 0
        
        for child in g:
            
            while cookieIdx < len(s) and s[cookieIdx] < child:
                cookieIdx += 1
            
            if cookieIdx == len(s):
                break 
            else:
                cookieIdx += 1
                res += 1
        
        return res
        
        