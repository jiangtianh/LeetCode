class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sortedarr = sorted(arr)
        d = {}
        c = 1
        for i, n in enumerate(sortedarr):
            if n not in d:
                d[n] = c
                c += 1
        res = [d[n] for n in arr]
        return res