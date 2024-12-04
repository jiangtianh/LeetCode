class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        
        if len(str2) > len(str1):
            return False
        
        def getOrd(c):
            return ord(c) - ord("a")
        

        j = 0
        for i, c in enumerate(str1):
            if j == len(str2):
                break
            if c == str2[j]:
                j += 1
                continue

            if (getOrd(c) + 1) % 26 == getOrd(str2[j]):
                j += 1
        
        return j == len(str2)