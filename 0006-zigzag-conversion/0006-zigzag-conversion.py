class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        res = [""] * numRows
        
        direction = -1
        pointer = 0
        
        for i in range(len(s)):
            c = s[i]
            res[pointer] += c
            
            if pointer == 0 or pointer == len(res) - 1:
                direction *= -1
            
            pointer += direction
            
        
        return "".join(res)
        
        
        