class Solution:
    def findScore(self, nums: List[int]) -> int:
        li = [[num, i] for i, num in enumerate(nums)]
        li.sort()   
        res = 0
        mark = set()

        for num, i in li:
            if i in mark:
                continue
            res += num
            mark.add(i)
            mark.add(i+1)
            mark.add(i-1)

        return res