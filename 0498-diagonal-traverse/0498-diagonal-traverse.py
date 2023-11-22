class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d = collections.defaultdict(list)

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                d[i + j].append(mat[i][j])
                
        idx = 0
        res = []
        for i in range(len(mat) + len(mat[0])):
            if idx % 2 == 0:
                d[i].reverse()
            res.extend(d[i])
            idx += 1
        
        return res



