class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        res = sum(piles)
        piles = [-pile for pile in piles]
        heapq.heapify(piles)

        for _ in range(k):
            num = -heapq.heappop(piles)

            toRemove = floor(num / 2)
            res -= toRemove

            heapq.heappush(piles, -(num - toRemove))

        return res
