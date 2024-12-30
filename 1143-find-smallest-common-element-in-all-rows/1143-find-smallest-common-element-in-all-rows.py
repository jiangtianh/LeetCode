class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        counter = collections.Counter()

        for li in mat:
            for n in li:
                counter[n] += 1
        
        res = math.inf 
        for n in counter:
            if counter[n] == len(mat):
                res = min(res, n)
        if res == math.inf:
            return -1
        return res