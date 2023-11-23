class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort() 
        res = len(points)
        
        l, r = -math.inf, -math.inf
        
        print(points)
        
        for x, y in points:
            
            if x > r:
                l = x
                r = y
                
            else:
                l = max(l, x)
                r = min(r, y)
                res -= 1
                
        return res
            
            
        