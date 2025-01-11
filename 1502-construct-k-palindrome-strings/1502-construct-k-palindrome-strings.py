class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        counter = collections.Counter(s)

        oddCount = 0
        for c in counter:
            if counter[c] % 2 == 1:
                oddCount += 1
                
 
        return oddCount <= k