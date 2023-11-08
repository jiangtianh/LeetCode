class Solution:
    def decodeString(self, s: str) -> str:
        res = ""

        stack = []
        i = 0

        while i < len(s):
            c = s[i]
            if c != "]":
                stack.append(c)
            else:
                temp = ""
                
                while True:
                    char = stack.pop() 
                    if char == "[":
                        num = ""
                        while stack and stack[-1].isnumeric():
                            num = stack.pop() + num
                        temp = temp * int(num)
                        if stack:

                            for j in range(len(temp)):
                                stack.append(temp[j])
                        else:
                            res += temp
                        
                        break

                    else:
                        temp = char + temp


            i += 1
        temp = ""
        while stack:
            temp = stack.pop() + temp
        res += temp

        return res
        

