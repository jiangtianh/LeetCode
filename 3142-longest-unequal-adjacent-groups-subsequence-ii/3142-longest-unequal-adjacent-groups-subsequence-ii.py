class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def hammingDistanceIsOne(i, j):
            if len(words[i]) != len(words[j]):
                return False
            c = 0
            for idx in range(len(words[i])):
                if words[i][idx] != words[j][idx]:
                    c += 1
                    if c == 2:
                        return False
            return c == 1
        n = len(words)
        dp = [1] * n

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if hammingDistanceIsOne(i, j) and groups[i] != groups[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        maxLength = max(dp)
        startIdx = dp.index(maxLength)
        currentIdx = startIdx
        res = [words[startIdx]]

        for i in range(startIdx + 1, n):
            if hammingDistanceIsOne(currentIdx, i) and groups[currentIdx] != groups[i] and dp[currentIdx] == dp[i] + 1:
                res.append(words[i])
                currentIdx = i

        return res