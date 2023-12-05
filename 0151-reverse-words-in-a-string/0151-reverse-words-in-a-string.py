class Solution:
    def reverseWords(self, s: str) -> str:
        temp = ""
        li = []
        for i in range(len(s)):
            c = s[i]

            if c == " ":
                if temp != "":
                    li.append(temp)
                    temp = ""
            else:
                temp += c

        if temp != "":
            li.append(temp)
        
        li.reverse()
        return " ".join(li)



