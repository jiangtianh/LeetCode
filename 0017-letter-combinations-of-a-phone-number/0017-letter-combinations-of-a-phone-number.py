class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        self.res = []
        
        def f(i, temp):
            if i >= len(digits):
                self.res.append("".join(temp))
                return 
            
            for c in d[digits[i]]:
                temp.append(c)
                f(i + 1, temp)
                temp.pop() 
                
            
        f(0, [])
        return self.res
        