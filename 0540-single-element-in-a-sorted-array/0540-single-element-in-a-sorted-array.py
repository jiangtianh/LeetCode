class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if 0 <= m - 1 < len(nums) and nums[m-1] == nums[m]:
                leftElem = m - 1 - l 
                rightElem = r - m
                if leftElem % 2 == 1:
                    r = m - 1 - 1
                else:
                    l = m + 1
            elif 0 <= m + 1 < len(nums) and nums[m+1] == nums[m]:
                leftElem = m - l 
                rightElem = r - m - 1
                if leftElem % 2 == 1:
                    r = m - 1
                else:
                    l = m + 1 + 1
            else:
                return nums[m]