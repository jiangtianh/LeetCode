class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        m = n // 2

        s = set()

        for candy in candyType:
            if candy not in s:
                s.add(candy)
            
            if len(s) == m:
                break
        
        return len(s)