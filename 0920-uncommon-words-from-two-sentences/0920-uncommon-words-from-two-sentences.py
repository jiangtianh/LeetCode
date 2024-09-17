class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split(" ")
        s2 = s2.split(" ")
        d = collections.defaultdict(int)

        for w in s1:
            d[w] += 1
        for w in s2:
            d[w] += 1

        res = []
        for w in d:
            if d[w] == 1:
                res.append(w)
        return res