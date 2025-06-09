class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        res = []

        def f(num):
            if num > n:
                return 
            res.append(num)
            
            num *= 10
            
            for i in range(10):
                f(num + i)
        
        for i in range(1, 10):
            f(i)
        return res