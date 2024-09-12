class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        res = 0
        broken = set(brokenLetters)
        text = text.split(' ')
        def check(s):
            for c in s:
                if c in broken:
                    return False
            return True

        for s in text:
            if check(s):
                res += 1

        return res