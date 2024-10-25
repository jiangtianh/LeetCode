class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        n = len(nums)

        heap = []
        d = collections.defaultdict(int)
        res = []

        for num, f in zip(nums, freq):
            d[num] += f
            while heap and d[heap[0][1]] + heap[0][0] != 0:
                heapq.heappop(heap)
            
            
            heapq.heappush(heap, [-d[num], num])

            if heap:
                res.append(-heap[0][0])
            else:
                res.append(0)

        return res