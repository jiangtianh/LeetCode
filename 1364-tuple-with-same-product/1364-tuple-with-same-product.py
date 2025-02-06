class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        d = collections.defaultdict(int)
        res = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                product = nums[i] * nums[j]
                if product in d:
                    res += d[product] * 8
                d[product] += 1
        return res