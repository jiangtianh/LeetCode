class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        @cache
        def f(x, y):
            if x == len(matrix):
                return 0
            
            if y not in range(len(matrix[0])):
                return math.inf
            
            
            
            return matrix[x][y] + min(f(x+1, y-1), f(x+1, y), f(x+1, y+1))
            
        res = math.inf
        for y in range(len(matrix[0])):
            res = min(res, f(0, y))
        
        return res