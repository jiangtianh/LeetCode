class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for c in magazine:
            d[c] = d.get(c, 0) + 1

        for c in ransomNote:
            if c in d:
                d[c] -= 1
                if d[c] < 0:
                    return False 

            else:
                return False

        return True