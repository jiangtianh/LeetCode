class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = [0] * (len(words) + 1)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0

        for i, word in enumerate(words):
            prefix[i] = count
            if word[0] in vowels and word[-1] in vowels:
                count += 1        
        prefix[-1] = count

        res = [0] * len(queries)

        for i, (l, r) in enumerate(queries):
            res[i] = prefix[r+1] - prefix[l]
        return res