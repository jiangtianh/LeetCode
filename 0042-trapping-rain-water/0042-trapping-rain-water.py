class Solution:
    def trap(self, height: List[int]) -> int:
        
        left = [0] * len(height)
        right = [0] * len(height)
        
        most = height[0]
        for i in range(1, len(height)):
            left[i] = most
            most = max(most, height[i])
        
        most = height[-1]
        for i in range(len(height) - 2, -1, -1):
            right[i] = most 
            most = max(most, height[i])
        
        res = 0
        for i in range(len(height)):
            temp = min(left[i], right[i]) - height[i]
            if temp > 0:
                res += temp
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        