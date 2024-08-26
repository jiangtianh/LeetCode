class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        self.res = []
        self.temp = []

        def f(i):
            if i == len(word):
                self.res.append("".join(self.temp))
                return 
            
            self.temp.append(word[i])
            f(i+1)
            self.temp.pop()
        
            if not self.temp or self.temp[-1].isalpha():
                self.temp.append("1")
                f(i+1)
                self.temp.pop()
            else:
                self.temp[-1] = str(int(self.temp[-1]) + 1)
                f(i+1)
        
        f(0)
        return self.res
            
                

        f(0)
        return self.res