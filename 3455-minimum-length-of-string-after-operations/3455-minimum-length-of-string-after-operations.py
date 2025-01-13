class Solution:
    def minimumLength(self, s: str) -> int:
        res = len(s)
        counter = collections.Counter(s)
        print(counter)
        for c in counter:
            if counter[c] > 2:
                if counter[c] % 2 == 1:
                    res -= counter[c] - 1
                else:
                    res -= counter[c] - 2

        return res 