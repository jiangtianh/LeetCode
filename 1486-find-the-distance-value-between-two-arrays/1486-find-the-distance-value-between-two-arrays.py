class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        
        def search(n):
            l = 0
            r = len(arr2) - 1
            while l <= r:
                m = (l + r) // 2
                num = abs(n - arr2[m])
                if num <= d:
                    return 1
                elif arr2[m] > n:
                    r = m - 1
                elif arr2[m] < n:
                    l = m + 1
            return 0
        res = len(arr1)
        for n in arr1:
            res -= search(n)
        return res
