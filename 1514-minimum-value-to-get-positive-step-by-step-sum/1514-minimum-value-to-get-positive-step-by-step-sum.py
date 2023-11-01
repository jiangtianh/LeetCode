class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = []
        cur = 0
        for num in nums:
            cur += num
            prefix.append(cur)

        smallest = min(prefix)

        print(smallest)
        if smallest < 0:
            return - (smallest - 1)
        else:
            return 1