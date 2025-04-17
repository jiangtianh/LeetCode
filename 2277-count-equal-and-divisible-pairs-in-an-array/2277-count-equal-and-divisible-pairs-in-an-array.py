class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        d = collections.defaultdict(list)
        res = 0

        for i, num in enumerate(nums):
            for idx in d[num]:
                if (idx * i) % k == 0:
                    res += 1

            d[num].append(i)
            
        return res