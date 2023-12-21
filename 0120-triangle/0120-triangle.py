class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @cache
        def f(level, i):
            if level == len(triangle):
                return 0 
            
            return min(f(level+1, i), f(level+1, i+1)) + triangle[level][i]

        return f(0, 0)
        
        