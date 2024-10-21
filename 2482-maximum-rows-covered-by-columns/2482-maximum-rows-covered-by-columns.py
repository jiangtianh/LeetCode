class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        s = set()
        m = len(matrix)
        n = len(matrix[0])
        res = 0

        def check():
            res = 0
            for i in range(m):
                haveOne = False
                for j in range(n):
                    if matrix[i][j] == 1 and j not in s:
                        haveOne = True
                        break
                if not haveOne:
                    res += 1
            return res
                    
        
        def f(i):
            nonlocal numSelect, res
            if i == n or numSelect == 0:
                res = max(res, check())
                return
            for j in range(i, n):
                numSelect -= 1
                s.add(j)
                f(j+1)
                s.remove(j)
                numSelect += 1

        f(0)
        return res
        
            