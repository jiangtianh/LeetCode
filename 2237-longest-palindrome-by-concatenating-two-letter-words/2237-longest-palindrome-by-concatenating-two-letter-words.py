class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = collections.defaultdict(int)
        res = 0
        for word in words:
            reverse = word[1] + word[0]
            if counter[reverse] > 0:
                counter[reverse] -= 1
                res += 4
            else:
                counter[word] += 1
        
        for word in counter:
            if word[0] == word[1] and counter[word] > 0:
                res += 2
                break
        return res