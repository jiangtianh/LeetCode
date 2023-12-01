class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        
        for i in range(1, len(strs)):
            s = strs[i]
            
            j = 0
            while j < len(prefix) and j < len(s) and s[j] == prefix[j]:
                j += 1
                
            prefix = prefix[:j]
        
        return prefix
        
        
        