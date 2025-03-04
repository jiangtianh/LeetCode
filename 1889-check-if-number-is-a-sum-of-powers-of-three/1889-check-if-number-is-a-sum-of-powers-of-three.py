class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        while n > 0:
            mod = n % 3
            if mod == 2:
                return False

            n //= 3
        
        return True