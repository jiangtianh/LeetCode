class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        temp = nums[:]
        heapq.heapify(temp)

        for _ in range(len(nums) - k):
            heapq.heappop(temp)
        
        d = {}
        for num in temp:
            d[num] = d.get(num, 0) + 1
        
        res = []
        for num in nums:
            if num in d and d[num] > 0:
                res.append(num)
                d[num] -= 1
        
        return res