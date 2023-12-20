class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
     
        
        for x in reversed(range(len(grid))):
            for y in reversed(range(len(grid[0]))):
                
                if x == len(grid) - 1 and y == len(grid[0]) - 1:
                    grid[x][y] = grid[x][y] 
                elif x == len(grid) - 1:
                    grid[x][y] = grid[x][y] + grid[x][y+1]
                elif y == len(grid[0]) - 1:
                    grid[x][y] = grid[x][y] + grid[x+1][y]
                else:
                    grid[x][y] = grid[x][y] + min(grid[x+1][y], grid[x][y+1])
        
        return grid[0][0]
        
        
        
        
     
            
            
            