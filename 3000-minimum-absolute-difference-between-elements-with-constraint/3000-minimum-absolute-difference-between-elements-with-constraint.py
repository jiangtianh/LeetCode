from sortedcontainers import SortedList

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        bst = SortedList()
        n = len(nums)
        res = math.inf 

        for i in range(n):
            if i - x >= 0:
                bst.add(nums[i-x])
            
            idx = bst.bisect_left(nums[i])
            if 0 <= idx < len(bst):
                res = min(res, bst[idx] - nums[i])
            if 0 <= idx - 1 < len(bst):
                res = min(res, nums[i] - bst[idx-1])
        return res