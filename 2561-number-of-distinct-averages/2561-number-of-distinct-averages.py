class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        s = set()

        while l < r:
            lnum = nums[l]
            rnum = nums[r]
            l += 1
            r -= 1
            s.add((lnum + rnum) / 2)

        return len(s)