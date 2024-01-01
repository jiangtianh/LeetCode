class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        
        d = collections.Counter(nums1)
        res = []
        for num in nums2:
            if num in d and d[num] > 0:
                res.append(num)
                d[num] -= 1
        
        return res

        