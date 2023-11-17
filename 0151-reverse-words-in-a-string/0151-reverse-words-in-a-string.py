class Solution:
    def reverseWords(self, s: str) -> str:
        
        temp = ""
        li = []
        
        for i in range(len(s)):
            if s[i] == " ":
                if temp != "":
                    li.append(temp)
                    temp = ""
                    
            else:
                temp += s[i]
        if temp:
            li.append(temp)
        
        print(li)
        
        li.reverse() 
        return " ".join(li)