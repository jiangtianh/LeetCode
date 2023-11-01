class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = nums[0] + nums[1] + nums[2]
        nums.sort()

        for i in range(len(nums)):
            num = nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = num + nums[l] + nums[r]
                if abs(total - target) < abs(res - target):
                    res = total
                if total < target:
                    l += 1
                else:
                    r -= 1
        
        return res