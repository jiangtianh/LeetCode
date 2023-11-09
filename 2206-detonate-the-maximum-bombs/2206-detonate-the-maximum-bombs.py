class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def getDistance(ax, ay, bx, by):
            return math.sqrt(abs(ax - bx) ** 2 + abs(ay - by) ** 2)

        def dfs(i, visited):
            res = 1
            for j in range(len(bombs)):
                bomb = bombs[j]
                if j not in visited and bombs[i][2] >= getDistance(bombs[i][0], bombs[i][1], bomb[0], bomb[1]):
                    visited.add(j)
                    res += dfs(j, visited)
            return res

        res = 0
        for i, bomb in enumerate(bombs):
            res = max(res, dfs(i, {i}))

        return res