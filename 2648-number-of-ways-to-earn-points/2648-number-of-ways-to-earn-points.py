class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        
        @cache
        def f(i, n):
            if n == 0:
                return 1
            elif i == len(types) or n < 0:
                return 0
            
            res = f(i+1, n)
            count, mark = types[i]
            for j in range(1, count + 1):
                res += f(i+1, n - j * mark)
            
            return res % (10 ** 9 + 7)

        return f(0, target) 
            
