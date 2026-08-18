class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return max(nums)
        
        if k == 1:
            counter = collections.Counter(nums)
            res = -math.inf
            for n in nums:
                if n > res and counter[n] == 1:
                    res = n
            return res if res != -math.inf else -1
        
        left = nums[0]
        right = nums[-1]

        if nums.count(left) != 1:
            left = -math.inf 
        if nums.count(right) != 1:
            right = -math.inf 

        res = max(left, right)

        if res == -math.inf:
            return -1
        return res