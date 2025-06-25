class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        candidates = [
            nums1[0] * nums2[0],
            nums1[0] * nums2[-1],
            nums1[-1] * nums2[0],
            nums1[-1] * nums2[-1]
        ]
        low, high = min(candidates), max(candidates)

        def f(mid):
            res = 0
            for a in nums1:
                if a == 0:
                    if mid >= 0:
                        res += len(nums2)
                elif a > 0:
                    t = mid / a
                    idx = bisect.bisect_right(nums2, math.floor(t))
                    res += idx
                elif a < 0:
                    t = mid / a
                    idx = bisect.bisect_left(nums2, math.ceil(t))
                    res += len(nums2) - idx
            return res
        res = high
        while low <= high:
            mid = (low + high) // 2
            if f(mid) >= k:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res