class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)

        for _ in range(k):
            cur = -heapq.heappop(gifts)

            cur = math.floor(math.sqrt(cur))
  
            heapq.heappush(gifts, -cur)

        return -sum(gifts)