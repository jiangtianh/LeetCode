class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        res = []
        idx = 0
        for i, c in enumerate(s):
            if idx < len(spaces) and spaces[idx] == i:
                res.append(" ")
                idx += 1
            res.append(c)

        return "".join(res)