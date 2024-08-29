class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        
        n = len(s)
        if n % 2 == 1:
            return False 
        free, count = 0, 0
        for i in range(n):
            c = s[i]
            if locked[i] == "1":
                if c == "(":
                    count += 1
                else:
                    count -= 1
            else:
                free += 1
            if count + free < 0:
                return False
        if count > free:
            return False
        
        free, count = 0, 0
        for i in range(n-1, -1, -1):
            c = s[i]
            if locked[i] == "1":
                if c == ")":
                    count += 1
                else:
                    count -= 1
            else:
                free += 1
            if count + free < 0:
                return False
        if count > free:
            return False

        return True