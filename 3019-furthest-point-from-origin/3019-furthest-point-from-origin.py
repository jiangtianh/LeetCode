class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        a = 0
        d = 0

        for c in moves:
            if c == "_":
                a += 1
            elif c == "L":
                d -= 1
            else:
                d += 1
        
        return max(abs(d - a), abs(d + a))