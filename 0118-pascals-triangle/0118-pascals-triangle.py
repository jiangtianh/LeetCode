class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        

        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        
        prev = self.generate(numRows - 1)

        res = [1]
        for i in range(len(prev[-1])-1):
            res.append(prev[-1][i] + prev[-1][i+1])
        
        res.append(1)
        prev.append(res)
        return prev