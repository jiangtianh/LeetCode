class Solution:
    def findScore(self, nums: List[int]) -> int:
        li = [[num, i] for i, num in enumerate(nums)]
        heapq.heapify(li)
        mark = set()
        score = 0
        
        while li:
            num, idx = heapq.heappop(li)
            if idx in mark:
                continue 
            
            score += num
            mark.add(idx)
            mark.add(idx + 1)
            mark.add(idx - 1)
        
        return score