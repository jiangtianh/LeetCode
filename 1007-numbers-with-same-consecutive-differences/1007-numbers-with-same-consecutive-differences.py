class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        self.res = []

        def f(prev, temp):
            
            if len(temp) == n:
                self.res.append(int("".join(temp)))
                return 
            
            avilableNum = []
            if k == 0:
                temp.append(str(prev))
                f(prev, temp)
                temp.pop()

                return 

            if prev + k < 10:
                avilableNum.append(prev + k)
            if prev - k >= 0:
                avilableNum.append(prev - k)
            
            
            for num in avilableNum:
                temp.append(str(num))
                f(num, temp)
                temp.pop() 
            


        
        for i in range(1, 10):
            f(i, [str(i)])
        
        return self.res





