class Solution:
    def minSteps(self, n: int) -> int:

        self.d = {}

        
        def f(n):
            if n == 1:
                return 0

            if n in self.d:
                return self.d[n]
            res = math.inf 
            
            for i in range(2, (n // 2) + 1):
                if n % i == 0:
                    res = min(res, f(n//i) + i)
            
            if res == math.inf:
                self.d[n] = n
                return n
            else:
                self.d[n] = res
                return res
            

        return f(n)