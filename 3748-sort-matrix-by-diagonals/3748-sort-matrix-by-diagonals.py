class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        
        n = len(grid)

        startingX, startingY = 0, n-1

        while startingX < n:
            temp = []
            x, y = startingX, startingY
            while x < n and y < n:
                temp.append(grid[x][y])
                x += 1
                y += 1
            
            temp.sort(reverse=startingY == 0)
            i = 0
            x, y = startingX, startingY
            while x < n and y < n:
                grid[x][y] = temp[i]
                i += 1
                x += 1
                y += 1
        

            if startingY != 0:
                startingY -= 1
            else:
                startingX += 1
        
        return grid