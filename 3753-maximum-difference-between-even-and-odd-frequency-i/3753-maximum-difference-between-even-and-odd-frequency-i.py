class Solution:
    def maxDifference(self, s: str) -> int:
        counter = collections.Counter(s)
        even = math.inf
        odd = -math.inf

        for c in counter:
            if counter[c] % 2 == 0:
                even = min(even, counter[c])
            else:
                odd = max(odd, counter[c])
        
        return odd - even