class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        res = 0
        for _ in range(k):
            score = -heapq.heappop(nums)
            res += score
            heapq.heappush(nums, - math.ceil(score/3))

        return res