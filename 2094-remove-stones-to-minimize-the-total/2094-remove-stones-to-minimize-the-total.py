class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        piles = [-i for i in piles]

        heapq.heapify(piles)

        for _ in range(k):
            cur = -heapq.heappop(piles)
            remove = cur // 2
            cur = - (cur - remove)
            heapq.heappush(piles, cur)

        return -sum(piles)

