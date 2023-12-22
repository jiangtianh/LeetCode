class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        x1, y1 = coordinates[0][0], coordinates[0][1]
        x2, y2 = coordinates[1][0], coordinates[1][1]
        
  
            
        
       
        for i in range(2, len(coordinates)):
            
            x3, y3 = coordinates[i]
            if (y3 - y1) * (x2 - x1) != (y2 - y1) * (x3 - x1):
                return False 
            
            
            
        return True
        
        
        