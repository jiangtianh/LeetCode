class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for i, word in enumerate(words):
            if word.count(x) > 0:
                res.append(i)
        return res