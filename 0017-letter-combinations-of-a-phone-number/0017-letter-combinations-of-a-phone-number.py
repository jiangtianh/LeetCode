class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        self.res = []

        def f(i, temp):
            if i == len(digits):
                self.res.append(temp)
                return

            for c in self.map[digits[i]]:
                temp += c
                f(i + 1, temp)
                temp = temp[:-1]
        
        if len(digits) == 0:
            return []
            
        f(0, "")
        return self.res