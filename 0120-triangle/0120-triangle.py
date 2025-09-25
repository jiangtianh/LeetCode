class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        @cache
        def f(i, j):
            if i == len(triangle):
                return 0
            
            return min(f(i+1, j), f(i+1, j+1)) + triangle[i][j]

        return f(0, 0)
