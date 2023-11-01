class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid -1

        return nums[l]