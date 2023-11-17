class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = {"a", "e", "i", "o", "u"}
        order = []
        word = []
        for i in range(len(s)):
            if s[i].lower() in vowel:
                order.append(i)
            word.append(s[i])
        
        l = 0
        r = len(order) - 1
        
        s.split()
        
        while l < r:
            word[order[l]], word[order[r]] = word[order[r]], word[order[l]] 
            l += 1
            r -= 1
        
        return "".join(word)