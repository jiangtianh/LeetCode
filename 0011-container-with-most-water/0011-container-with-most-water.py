class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        def calculate(l, r):
            return (r - l) * min(height[l], height[r])
        
        
        l = 0 
        r = len(height) - 1
        
        res = 0
        
        while l < r:
            res = max(res, calculate(l, r))
            if height[l] < height[r]:
                l += 1
            else: 
                r -= 1
        
        return res