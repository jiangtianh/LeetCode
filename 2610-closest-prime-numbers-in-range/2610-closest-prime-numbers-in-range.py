from math import *
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def isPrime(num):
            for i in range(2, floor(sqrt(num)) + 1):
                if num / i == num // i:
                    return False
            return True


        prev = None 
        res = [0, right + 2]

        for i in range(max(left, 2), right + 1):
            if isPrime(i):
                if prev:
                    if i - prev < res[1] - res[0]:
                        res = [prev, i]
                    if i - prev <= 2:
                        return res
                prev = i
        
        if res[0] == 0:
            return [-1, -1]
        return res