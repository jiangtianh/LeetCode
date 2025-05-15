class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        prev = -1
        res = []

        for i in range(n):
            if prev != groups[i]:
                res.append(words[i])
                prev = groups[i]

        return res