class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        self.res = 0
        
        @cache
        def f(x, y):
            if x not in range(len(matrix)) or y not in range(len(matrix[0])):
                return 0
            
            bot = f(x + 1, y)
            right = f(x, y + 1)
            botright = f(x + 1, y + 1)
            
            if bot and right and botright:
                minimum = min(bot, right, botright)
                if matrix[x][y] == '1':
                    res = minimum + 1
                else:
                    res = 0
            else:
                res = int(matrix[x][y])
            
            self.res = max(self.res, res ** 2)
            return res

        
        f(0, 0)
        return self.res
            
        
            
            
            
            
            