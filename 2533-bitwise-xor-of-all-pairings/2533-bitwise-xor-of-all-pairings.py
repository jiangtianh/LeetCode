class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        
        if n % 2 == 0:
            res1 = 0
        else:
            res1 = 0
            for num in nums1:
                res1 ^= num

        if m % 2 == 0:
            res2 = 0
        else:
            res2 = 0
            for num in nums2:
                res2 ^= num

        return res1 ^ res2