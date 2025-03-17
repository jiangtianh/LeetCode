class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        width = sum(wall[0])

        d = {}
        for row in wall:
            c = 0
            for n in row[:-1]:
                c += n
                d[c] = d.get(c, 0) + 1
        print(d.values())
        return len(wall) - max(d.values()) if d.values() else len(wall)