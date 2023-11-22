class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        d = collections.defaultdict(list)

        


        for i in range(len(nums)):
            for j in range(len(nums[i])):
                d[i+j].append(nums[i][j])
        res = []
        print(max(d.keys()))
        print(d[0])
        for i in range(0, max(d.keys()) + 1):
            if d[i]:
                d[i].reverse()
                res.extend(d[i])
        
        return res

