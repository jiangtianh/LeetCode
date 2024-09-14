class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        b, r = 0, 0

        level = 1
        bc, rc = blue, red
        while True:
            if level % 2 == 1:
                if bc >= level:
                    bc -= level
                    level += 1
                else:
                    break
            else:
                if rc >= level:
                    rc -= level
                    level += 1
                else:
                    break
        b = level-1

        level = 1
        bc, rc = blue, red
        while True:
            if level % 2 == 1:
                if rc >= level:
                    rc -= level
                    level += 1
                else:
                    break
            else:
                if bc >= level:
                    bc -= level
                    level += 1
                else:
                    break
        r = level-1

        return max(r, b)


