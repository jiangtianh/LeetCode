class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rightMost1 = [-1] * n
        for i, row in enumerate(grid):
            
            for j in range(n-1, -1, -1):
                if row[j] == 1:
                    break
            rightMost1[i] = j
        
        sortedLi = sorted(rightMost1)
        print(sortedLi)
        for i in range(n):
            if sortedLi[i] > i:
                print('111')
                return -1

        res = 0
        i = 0
        while i < n:
            
            for j in range(i, n):
                if rightMost1[j] <= i:
                    break
            
            row = rightMost1.pop(j)
            rightMost1.insert(i, row)
            res += (j - i)

            i += 1
        
        return res


