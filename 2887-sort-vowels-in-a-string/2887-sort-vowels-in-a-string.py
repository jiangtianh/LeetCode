class Solution:
    def sortVowels(self, s: str) -> str:
        def isVowel(c):
            return c in {"A", "a", "E", "e", "I", "i", "O", "o", "U", "u"}

        vowels = []
        vowelIdx = set()
        for i in range(len(s)):
            if isVowel(s[i]):
                vowelIdx.add(i)
                vowels.append(s[i])
        
        vowels.sort()
        p = 0
        res = ""

        for i in range(len(s)):
            if i in vowelIdx:
                res += vowels[p]
                p += 1
            else:
                res += s[i]
        return res
