class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        res = 1
        
        for i in range(len(s)):
            window = {s[i]}
            if res > len(s) - i:
                break 
            for j in range(i+1, len(s)):
                if s[j] not in window:
                    window.add(s[j])
                    res = max(res, j - i + 1)
                else:
                    break 
        
        return res