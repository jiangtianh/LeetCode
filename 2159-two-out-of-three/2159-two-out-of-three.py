class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        c = collections.defaultdict(int)
        s1, s2, s3 = set(nums1), set(nums2), set(nums3)

        for n in s1:
            c[n] += 1
        for n in s2:
            c[n] += 1
        for n in s3:
            c[n] += 1
        res = []
        for n in c:
            if c[n] >= 2:
                res.append(n)
        return res