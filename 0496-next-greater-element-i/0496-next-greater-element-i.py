class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = [0]
        res = [-1] * len(nums2)

        for i in range(1, len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                res[stack.pop()] = nums2[i]
            stack.append(i)
        
        d = {}
        for i in range(len(nums2)):
            d[nums2[i]] = res[i]
        
        res = []
        for num in nums1:
            res.append(d[num])

        return res