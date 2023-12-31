class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0 
        
        for i in range(len(heights)):
            h = heights[i]
            
            idx = -1
            
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                res = max(res, (i - idx) * height)
            
            if idx != -1:
                stack.append((idx, h))
            else:
                stack.append((i, h))
                             
        
        for i, h in stack:
            res = max(res, h * (len(heights) - i))
            
       
            
        
        return res
            
        
        
        