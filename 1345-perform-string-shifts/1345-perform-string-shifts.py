class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        d = 0
        for direction, amount in shift:
            if direction == 0:
                d -= amount
            else:
                d += amount
        
        d = d % len(s)
        return s[len(s) - d:] + s[:len(s) - d]