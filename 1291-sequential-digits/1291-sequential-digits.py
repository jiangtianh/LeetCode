class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        minDigit = len(str(low))
        maxDigit = len(str(high))

        def check(num):
            return low <= num <= high
        
        def combineNum(li):
            res = 0
            for num in li:
                res = res * 10  + num 
            return res 

 
        res = []

        for digit in range(minDigit, maxDigit+1):
            temp = [i for i in range(1, digit+1)]
            
            for _ in range(9-temp[-1]+1):
                current = combineNum(temp)
                if check(current):
                    res.append(current)
                
                
                for i in range(len(temp)):
                    temp[i] += 1

        return res
