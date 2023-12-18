class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        res = [""] * numRows
        direction = 1
        i = 0
        for c in s:
            res[i] += c
            
            i += direction 
            
            if i < 0:
                i = 1
                direction *= -1
               
            if i == numRows:
                i = numRows - 2
                direction *= -1
                
        return "".join(res)
            
            