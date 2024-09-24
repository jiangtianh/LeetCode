class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        s = set()
        for num in arr1:
            while num > 0:
                s.add(num)
                num //= 10
        
        res = 0
        for num in arr2:
            while num > 0:
                if num in s:
                    res = max(res, len(str(num)))
                num //= 10
        return res