class Solution:
    def partitionLabels(self, str: str) -> List[int]:
        counter = collections.Counter(str)
        res = []
        s = set()
        l = 0

        def check(s):
            for char in s:
                if counter[char] > 0:
                    return False
            return True 

        for i, c in enumerate(str):
            counter[c] -= 1
            s.add(c)
            if check(s):
                res.append(i - l + 1)
                l = i+1
        
        return res