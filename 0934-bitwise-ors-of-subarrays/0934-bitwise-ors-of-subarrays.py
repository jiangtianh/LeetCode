class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        cur = set()

        for num in arr:
            newS = {num}
            for prev in cur:
                newS.add(prev | num)
            cur = newS
            res = res.union(cur)
        return len(res)