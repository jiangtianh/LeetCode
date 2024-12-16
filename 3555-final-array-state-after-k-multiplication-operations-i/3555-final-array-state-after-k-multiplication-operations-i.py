class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        nums = [[num, i] for i, num in enumerate(nums)]
        heapq.heapify(nums)

        for _ in range(k):
            n, i = heapq.heappop(nums)
            heapq.heappush(nums, [n * multiplier, i])
        
        nums.sort(key=lambda x: x[1])
        return [num for num, i in nums]
