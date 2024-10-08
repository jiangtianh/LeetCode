class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        d = collections.defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                d[nums[i] * nums[j]] += 1
        res = 0
        for n in d:
            if d[n] > 1:
                c = d[n]
                m = c * (c-1) // 2
                res += m * 8
        return res