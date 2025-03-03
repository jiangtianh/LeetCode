class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = []
        larger = []
        pivotcount = 0
        for n in nums:
            if n == pivot:
                pivotcount += 1
            elif n < pivot:
                smaller.append(n)
            else:
                larger.append(n)

        return smaller + [pivot] * pivotcount + larger