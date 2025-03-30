class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter = collections.Counter(s)
        current = set()
        l = 0
        res = []
        for r, c in enumerate(s):
            counter[c] -= 1
            current.add(c)
            allClear = True
            for char in current:
                if counter[char] != 0:
                    allClear = False
                    break
            if allClear:
                res.append(r - l + 1)
                l = r + 1
        
        return res