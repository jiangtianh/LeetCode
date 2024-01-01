class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort() 
        flag = [True] * len(s)
        
        res = 0
        
        for child in g:
            for i, cookie in enumerate(s):
                if cookie >= child and flag[i]:
                    res += 1
                    flag[i] = False
                    break
        
        return res