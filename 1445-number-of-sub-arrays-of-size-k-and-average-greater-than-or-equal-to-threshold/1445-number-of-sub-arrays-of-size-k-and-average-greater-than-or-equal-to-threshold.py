class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        r = k - 1
        total = sum(arr[:k-1])
        res = 0
        while r < len(arr):
            total += arr[r]
            if total // k >= threshold:
                res += 1
            
            total -= arr[l]
            r += 1
            l += 1
        return res