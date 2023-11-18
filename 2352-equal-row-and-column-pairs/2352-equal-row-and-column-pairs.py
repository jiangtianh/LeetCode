class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d = {}
        d2 = {}
        
        for i in range(len(grid)):
            temp = ""
            temp2 = ''
            for j in range(len(grid)):
                temp += str(grid[i][j]) + ","
                temp2 += str(grid[j][i]) + ","
            
            d[temp] = d.get(temp, 0) + 1
            d2[temp2] = d2.get(temp2, 0) + 1
            
        res = 0
        for key in d:
            if key in d2:
                res += d[key] * d2[key]
            
            
        return res
        
        
            