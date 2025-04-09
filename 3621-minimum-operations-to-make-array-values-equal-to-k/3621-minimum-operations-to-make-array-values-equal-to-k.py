class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        counter = collections.Counter(nums)

        if min(counter.keys()) < k:
            return -1
        elif min(counter.keys()) == k:
            return len(counter.keys()) - 1
        else:
            return len(counter.keys())