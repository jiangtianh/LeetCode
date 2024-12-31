class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = collections.defaultdict(int)
        for c in s:
            counter[c] += 1
        
        odd = 0
        for c in counter:
            if counter[c] % 2 == 1:
                odd += 1
        return odd <= 1