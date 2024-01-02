class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        set1 = set(nums1)
        
        res = math.inf 
        nums2.sort()
        for num in nums2:
            if num in set1:
                return num 
        
        nums1.sort() 
        
        if nums1[0] > nums2[0]:
            return nums2[0] * 10 + nums1[0]
        else:
            return nums1[0] * 10 + nums2[0]
        
                
        