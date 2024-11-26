class SparseVector:
    def __init__(self, nums: List[int]):
        self.vec = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:

        res = 0
        for x, y in zip(self.vec, vec.vec):
            res += x * y
        return res



# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)