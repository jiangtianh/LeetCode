class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = "balloon"
        d = {}
        for c in text:
            d[c] = d.get(c, 0) + 1

        res = 0

        while True:
            for c in balloon:
                if c not in d:
                    return res
                d[c] -= 1
                if d[c] < 0:
                    return res

            res += 1

        return res