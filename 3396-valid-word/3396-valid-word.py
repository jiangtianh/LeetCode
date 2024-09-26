class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowels = {'a','e','i','o','u', 'A', 'E', 'I', 'O', 'U'}
        vowelCount = 0
        consonantCount = 0

        for c in word:
            if c.isalpha():
                if c in vowels:
                    vowelCount += 1
                else:
                    consonantCount += 1
            
            elif not c.isnumeric():
                return False
        
        return vowelCount != 0 and consonantCount != 0