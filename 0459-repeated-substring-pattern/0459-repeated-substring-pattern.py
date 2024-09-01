class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = 1

        while length <= len(s) // 2:
            
            if len(s) % length != 0:
                length += 1
                continue 

            subS = s[:length]
            temp = subS * (len(s) // length) 

            if temp == s:
                return True 

            length += 1
        
        return False