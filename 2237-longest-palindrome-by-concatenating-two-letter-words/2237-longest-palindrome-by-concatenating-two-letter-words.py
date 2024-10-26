class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        reverse = collections.defaultdict(int)
        same = collections.defaultdict(int)

        res = 0
        for w in words:
            
            revW = w[1] + w[0]
            if reverse[revW] > 0:
                res += 4
                reverse[revW] -= 1
            else:
                reverse[w] += 1
        
        for w in reverse:
            if w[1] == w[0] and reverse[w] > 0:
                res += 2
                return res
        return res