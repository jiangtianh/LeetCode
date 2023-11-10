class Solution:
    def judgeCircle(self, moves: str) -> bool:
        horizontal = vertical = 0

        for c in moves:
            if c == "U":
                vertical += 1
            elif c == "D":
                vertical -= 1
            elif c == "L":
                horizontal -= 1
            elif c == "R":
                horizontal += 1
        
        return horizontal == 0 and vertical == 0