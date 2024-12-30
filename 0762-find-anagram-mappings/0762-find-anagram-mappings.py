class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idx = collections.defaultdict(collections.deque)

        for i, n in enumerate(nums2):
            idx[n].append(i)
        
        res = []

        for n in nums1:
            res.append(idx[n].popleft())
        return res