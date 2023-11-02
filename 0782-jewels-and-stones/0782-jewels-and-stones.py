class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set() 

        for c in jewels:
            s.add(c)

        res = 0
        for c in stones:
            if c in s:
                res += 1
        
        return res