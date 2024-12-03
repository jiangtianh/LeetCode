class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        res = []

        start = 0
        for j in spaces:
            res.append(s[start:j])
            start = j
        res.append(s[start:])
        return " ".join(res)