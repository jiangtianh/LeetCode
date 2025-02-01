class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        d = {}
        l = 0
        res = []

        for r in range(len(nums)):
            d[nums[r]] = d.get(nums[r], 0) + 1
            
            if r - l + 1 == k:
                res.append(len(d))
                
                d[nums[l]] -= 1
                if d[nums[l]] == 0:
                    d.pop(nums[l])
                l += 1
        return res
