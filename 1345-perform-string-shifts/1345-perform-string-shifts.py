class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        d = 0
        for direction, amount in shift:
            if direction == 0:
                d -= amount
            else:
                d += amount
        print(d)
        
        d = d % len(s)
        print(d)
        return s[len(s) - d:] + s[:len(s) - d]