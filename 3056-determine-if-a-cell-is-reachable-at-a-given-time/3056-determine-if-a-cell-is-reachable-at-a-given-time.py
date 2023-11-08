class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:

        if sx == fx and sy == fy:
            return t != 1




        totalDistance = abs(sx - fx) + abs(sy- fy)

        sideWayMove = min(abs(sx - fx), abs(sy - fy))

        minMoveNeeded = totalDistance - sideWayMove

        return minMoveNeeded <= t