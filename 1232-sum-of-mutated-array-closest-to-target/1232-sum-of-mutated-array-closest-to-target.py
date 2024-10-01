class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        runningSum = [0]
        total = 0

        for n in arr:
            total += n
            runningSum.append(total)

        diff = math.inf
        res = math.inf

        l = 0
        r = arr[-1]
        print(arr)
        while l <= r:
            m = (l + r) // 2
            idx = bisect_left(arr, m)
            total = runningSum[idx] + (len(arr) - idx) * m
          
            if abs(total - target) < diff:
                diff = abs(total - target)
                res = m
            elif abs(total - target) == diff:
                res = min(res, m)            

            if total > target:
                r = m - 1
            else:
                l = m + 1
        return res
