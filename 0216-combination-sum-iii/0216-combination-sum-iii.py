class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []
        self.temp = []
        self.total = 0

        def f(j):
            if self.total > n:
                return 
            elif self.total == n and len(self.temp) == k:
                self.res.append(self.temp[:])
                return 
            
            for i in range(j, 10):
                self.total += i
                self.temp.append(i)
                f(i+1)
                self.temp.pop()
                self.total -= i
        
        f(1)
        return self.res