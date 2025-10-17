class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = [[-num, i] for i, num in enumerate(nums[:k])]
        heapq.heapify(heap)

        res = [-heap[0][0]]

        for i in range(k, len(nums)):
            heapq.heappush(heap, [-nums[i], i])
            while heap and heap[0][1] <= i - k:
                heapq.heappop(heap)
            
            res.append(-heap[0][0])

        return res