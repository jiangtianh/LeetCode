class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        def f(n):
            res = 0
            count = 0
            for d in range(1, int(sqrt(n)) + 1):
                if n % d == 0:
                    if d == n // d:
                        count += 1
                        res += d
                    else:
                        count += 2
                        res += d 
                        res += n // d
            if count == 4:
                return res
            else:
                return 0
            

        res = 0
        for n in nums:
            res += f(n)
        return res