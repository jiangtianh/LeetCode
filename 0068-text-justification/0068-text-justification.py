class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        tempWidthCounter = 0
        tempWindow = []
        res = []
        def process(window):
            if len(window) == 1:
                return window[0] + " " * (maxWidth - len(window[0]))

            result = []
            widthLeft = maxWidth
            for i in range(len(window)):
                result.append(window[i])
                widthLeft -= len(window[i])
                if i != len(window) - 1:
                    result.append(" ")
                    widthLeft -= 1
            idx = 1
            while widthLeft > 0:
                result[idx] += " "
                idx += 2
                if idx >= len(result):
                    idx = 1
                widthLeft -= 1

            return "".join(result)




        for word in words:
            tempWidthCounter += len(word)
            if tempWidthCounter > maxWidth:
                res.append(process(tempWindow))
                tempWindow = [word]
                tempWidthCounter = len(word) + 1
            else:
                tempWindow.append(word)
                tempWidthCounter += 1
        
        finalLine = " ".join(tempWindow)
        finalLine += " " * (maxWidth - len(finalLine))
        res.append(finalLine)
        return res