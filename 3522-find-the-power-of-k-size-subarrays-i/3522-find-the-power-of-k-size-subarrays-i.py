class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        cur = [nums[i] for i in range(k)]
        cur = deque(cur)
        
        def isConsecusitive(cur):
            for i in range(1, len(cur)):
                if cur[i-1] != cur[i] - 1:
                    return False
            return True 
        if isConsecusitive(cur):
            res = [cur[-1]]
        else:
            res = [-1]
        for i in range(k, len(nums)):
            cur.popleft()
            cur.append(nums[i])
            if isConsecusitive(cur):
                res.append(cur[-1])
            else:
                res.append(-1)
        return res