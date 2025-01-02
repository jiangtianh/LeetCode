class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        count = 0
        prefix = [0] * len(words)
        vowels = "aeiou"
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                count += 1
            prefix[i] = count

        res = []
        for l, r in queries:
            if l == 0:
                res.append(prefix[r])
            else:
                res.append(prefix[r] - prefix[l-1])
        return res