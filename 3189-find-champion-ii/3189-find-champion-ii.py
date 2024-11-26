class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        s = set()
        for x, y in edges:
            s.add(y)
        res = -1
        count = 0
        for i in range(n):
            if i not in s:
                res = i
                count += 1
                if count == 2:
                    return -1

        return res