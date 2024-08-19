class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        l = 0
        r = len(nums) - 1
        res = []
        while l <= r:
            res.append(nums[l])
            if len(res) == len(nums):
                break
            res.append(nums[r])
            l += 1
            r -= 1

        return res