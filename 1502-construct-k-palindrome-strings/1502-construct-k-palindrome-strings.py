class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        counter = collections.Counter(s)
        haveToHave = 0

        for c in counter:
            if counter[c] % 2 == 1:
                haveToHave += 1
        
        return haveToHave <= k