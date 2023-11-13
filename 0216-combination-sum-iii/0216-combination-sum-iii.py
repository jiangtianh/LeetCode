class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        self.res = []

        def f(idx, remain, visited, start):
            
            if idx == k and remain == 0:
                self.res.append(list(visited))
                return 
            if remain < 0 or idx >= k:
                return
            
            for i in range(start, 10):
                if i not in visited:
                    visited.add(i)
                    f(idx + 1, remain - i, visited, i + 1)
                    visited.remove(i)

        f(0, n, set(), 1)
        return self.res
                