class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        

        temp = ''
        for i in range(len(s1)):
            if i < len(s2) and s1[i] == s2[i] and i < len(s3) and s1[i] == s3[i]:
                temp += s1[i]
            else:
                break

        if not temp:
            return -1
        
        res = len(s1) + len(s2) + len(s3) - 3 * len(temp)
        return res