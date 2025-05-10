class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1Zero = 0
        nums1Sum = 0
        nums2Zero = 0
        nums2Sum = 0
        for num in nums1:
            if num == 0:
                nums1Zero += 1
            else:
                nums1Sum += num
        for num in nums2:
            if num == 0:
                nums2Zero += 1
            else:
                nums2Sum += num
        

        minimumNums1 = nums1Sum + nums1Zero
        minimumNums2 = nums2Sum + nums2Zero

        if minimumNums1 == minimumNums2:
            if nums1Sum < nums2Sum:
                if nums1Zero == 0:
                    return -1
            elif nums1Sum > nums2Sum:
                if nums2Zero == 0:
                    return -1
            return minimumNums1

        elif minimumNums1 > minimumNums2:
            if nums2Zero == 0:
                return -1
            return minimumNums1
        else:
            if nums1Zero == 0:
                return -1
            return minimumNums2


  