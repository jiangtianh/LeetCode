class Solution:
    def countElements(self, arr: List[int]) -> int:
        s = set()

        for i in arr:
            s.add(i)
        
        res = 0
        for i in arr:
            if i + 1 in s:
                res += 1

        return res