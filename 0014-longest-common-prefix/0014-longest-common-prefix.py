class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        prefix = ""
        
        while True:
            if i not in range(len(strs[0])):
                return prefix
            c = strs[0][i]
            
            for s in strs:
                if i >= len(s) or s[i] != c:
                    return prefix
            prefix += c
            i += 1
            
        return prefix
        
        
        
        