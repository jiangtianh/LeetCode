class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        d = {}
        l = 0
        res = 0

        for r, num in enumerate(nums):
            d[num] = d.get(num, 0) + 1

            while l < len(nums) and max(d) - min(d) > 2:
                d[nums[l]] -= 1
                if d[nums[l]] == 0:
                    d.pop(nums[l])
                l += 1
            
            res += r - l + 1
        
        return res