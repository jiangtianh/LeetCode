class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        
        N = len(nums)
        mins = nums[:]
        best = sum(nums)

        for i in range(N):
            current = i * x
            for j in range(N):
                mins[j] = min(mins[j], nums[(j + i) % N])
            best = min(best, sum(mins) + current)
        
        return best