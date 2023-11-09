class Solution:
    def countHomogenous(self, s: str) -> int:
        def count(i):
            return (i * (i + 1)) / 2
        
        
        mod = 10 ** 9 + 7
        
        res = 0
        
        i = 0
        while i < len(s):
            end = i
            while end != len(s) - 1 and s[end] == s[end+1]:
                end += 1
            
            res += count(end - i + 1)

            i = end + 1
        
        return int(res) % mod

