class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        shorter, longer = nums1, nums2
        if len(nums1) > len(nums2):
            shorter, longer = nums2, nums1
        
        d = collections.Counter(shorter)
        res = []
        for num in longer:
            if num in d and d[num] > 0:
                res.append(num)
                d[num] -= 1
        
        return res

        