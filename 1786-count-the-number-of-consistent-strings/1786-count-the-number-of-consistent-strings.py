class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allow = set(allowed)
        res = 0
        for word in words:
            newWord = set(word)
            if newWord.issubset(allow):
                res += 1
        return res