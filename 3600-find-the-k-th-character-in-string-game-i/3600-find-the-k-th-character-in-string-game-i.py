class Solution:
    def kthCharacter(self, k: int) -> str:
        s = [0]

        while len(s) < k:
            newS = []
            for c in s:
                newS.append(c+1)
            s = s + newS

        return chr(s[k-1] + ord("a"))
