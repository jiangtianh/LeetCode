class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        res = grid.copy() 
        
        for x in reversed(range(len(grid))):
            for y in reversed(range(len(grid[0]))):
                
                if x == len(grid) - 1 and y == len(grid[0]) - 1:
                    res[x][y] = grid[x][y] 
                elif x == len(grid) - 1:
                    res[x][y] = grid[x][y] + res[x][y+1]
                elif y == len(grid[0]) - 1:
                    res[x][y] = grid[x][y] + res[x+1][y]
                else:
                    res[x][y] = grid[x][y] + min(res[x+1][y], res[x][y+1])
        
        return res[0][0]
        
        
        
        
     
            
            
            