class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        li = []
        for i, n in enumerate(nums):
            if n == key:
                li.append(i)
            
        res = set()
        for j in li:
            for i in range(max(0, j-k), min(len(nums), j+k+1)):
                res.add(i)

        return list(res)
