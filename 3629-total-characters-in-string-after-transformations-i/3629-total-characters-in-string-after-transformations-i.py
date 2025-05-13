class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        d = collections.defaultdict(int)
        MOD = 10 ** 9 + 7
        for c in s:
            d[c] += 1

        
        def f(d):
            zCount = d["z"]
            d["z"] = 0
            for i in range(24, -1, -1):
                d[chr(i + ord("a") + 1)] = d[chr(i + ord("a"))]
            d["a"] = zCount
            d["b"] += zCount

        def down26(d):
            zCOunt = d["z"]
            for i in range(24, -1, -1):
                d[chr(i+ord("a") + 1)] += d[chr(i + ord("a"))]
            d["a"] += zCOunt
            d["b"] += zCOunt

        for _ in range(t // 26):
            down26(d)
        for _ in range(t % 26):
            f(d)


        print(d)
        return sum(d.values()) % MOD