class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = collections.defaultdict(int)
        d[0] = 1
        res = 0
        total = 0

        for n in nums:
            total += n
            remainder = total % k
            res += d[remainder]
            d[remainder] += 1
        return res