class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        res = 0 
        def isPrefixAndSuffix(w1, w2):
            if w2.startswith(w1) and w2.endswith(w1):
                return True
            return False
        for i in range(len(words)):
            for j in range(i):
                if isPrefixAndSuffix(words[j], words[i]):
                    res += 1
        return res