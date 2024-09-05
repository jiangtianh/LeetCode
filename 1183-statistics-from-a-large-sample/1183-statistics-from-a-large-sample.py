class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        minimum = 256
        maximum = -1
        totalSum = 0
        totalCount = 0
        def findKth(k, l, r):
            leftCount = 0
            m = (l + r) // 2
            for i in range(l, m):
                leftCount += count[i]
        
            if leftCount < k and leftCount + count[m] >= k:
                return m
            elif leftCount >= k:
                return findKth(k, l, m-1)
            elif leftCount + count[m] < k:
                return findKth(k - leftCount - count[m], m + 1, r)
            else:
                return findKth(k - leftCount, m, r)
        
        mode = 0
        modeNum = -1

        for i in range(256):
            if count[i]:
                minimum = min(minimum, i)
                maximum = max(maximum, i)
                totalSum += count[i] * i
                totalCount += count[i]
                if count[i] > mode:
                    mode = count[i]
                    modeNum = i
        mean = totalSum / totalCount
        if totalCount % 2 == 0:
            median = (findKth(totalCount // 2, 0, 255) + findKth(totalCount // 2 + 1, 0, 255)) / 2
        else:
            median = findKth(totalCount // 2 + 1, 0, 255)
        
        return [minimum, maximum, mean, median, modeNum]