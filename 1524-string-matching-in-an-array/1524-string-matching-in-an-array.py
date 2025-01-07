class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key= lambda x: -len(x))
        seen = set()
        res = []
        for word in words:
            for s in seen:
                if s.find(word) != -1:
                    res.append(word)
                    break
            seen.add(word)
        return res