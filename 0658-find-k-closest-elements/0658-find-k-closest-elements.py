class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        l, r = 0, n - 1

        while l <= r:
            m = (l + r) // 2
            if arr[m] >= x:
                r = m - 1
            else:
                l = m + 1

        r = l
        l = l - 1
        res = []
        for _ in range(k):
            if l >= 0 and r < n:
                if x - arr[l] <= arr[r] - x:
                    res.append(arr[l])
                    l -= 1
                elif x - arr[l] > arr[r] - x:
                    res.append(arr[r])
                    r += 1

            elif l >= 0:
                res.append(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1
        res.sort()
        return res
