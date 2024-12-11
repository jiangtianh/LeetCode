class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        i = 0
        j = 0

        while i < len(word) and j < len(abbr):
            if abbr[j].isalpha():
                if word[i] == abbr[j]:
                    i += 1
                    j += 1
                else:
                    return False
            else:
                if abbr[j] == "0":
                    return False
                s = ""
                while j < len(abbr) and abbr[j].isnumeric():
                    s += abbr[j]
                    j += 1
                i += int(s)
        
        return i == len(word) and j == len(abbr)