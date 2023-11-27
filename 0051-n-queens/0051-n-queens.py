class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        temp = [["."] * n for _ in range(n)]
        
        horizontal = [True] * n
        vertical = [True] * n
        leftDiagnal = [True] * (n * 2 - 1)
        rightDiagnal = set()
        
        def place(x, y):
            if horizontal[x] and vertical[y] and leftDiagnal[x+y] and (x, y) not in rightDiagnal:
                temp[x][y] = "Q"
                horizontal[x] = False 
                vertical[y] = False 
                leftDiagnal[x+y] = False
                while x > 0 and y > 0:
                    x -= 1
                    y -= 1
                while x < n and y < n:
                    rightDiagnal.add((x, y))
                    x += 1
                    y += 1
                return True 
            else:
                return False 
        
        def remove(x, y):
            temp[x][y] = "."
            horizontal[x] = True 
            vertical[y] = True 
            leftDiagnal[x+y] = True
            while x > 0 and y > 0:
                x -= 1
                y -= 1
            while x < n and y < n:
                rightDiagnal.remove((x, y))
                x += 1
                y += 1
        
        self.res = []
        
        def f(x, queensLeft):
            if queensLeft == 0:
                self.res.append(["".join(temp[i]) for i in range(len(temp))])
                return 
            if x >= n:
                return 
            
            for i in range(n):
                if place(x, i):
                    f(x + 1, queensLeft - 1)
                    remove(x, i)
            
        f(0, n)
        return self.res
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            