class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy = 0
        xz = 0
        zy = [0] * len(grid[0])
        
        for x in range(len(grid)):
            tempxz = 0
            for y in range(len(grid[0])):
                if grid[x][y] != 0:
                    xy += 1
                tempxz = max(tempxz, grid[x][y])
                zy[y] = max(zy[y], grid[x][y])
            
            xz += tempxz
            
        print(xy)
        print(xz)
        print(sum(zy))
        return xy + xz + sum(zy)