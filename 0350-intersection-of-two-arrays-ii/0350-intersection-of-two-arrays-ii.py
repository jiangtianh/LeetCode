class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1.sort() 
        nums2.sort()

        p = 0
        res = []
        
        for i in range(len(nums1)):
            
            while p < len(nums2) and nums2[p] < nums1[i]:
                p += 1
            if p < len(nums2) and nums2[p] == nums1[i]:
                res.append(nums1[i])
                p += 1
        
        return res
        
      
        
        
        
        