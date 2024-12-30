class Solution:
    def validWordSquare(self, words: List[str]) -> bool:

        x = 0
        y = 0

        while x < len(words):
            w1 = []
            for col in range(y+1, len(words[x])):
                w1.append(words[x][col])
            w2 = []
            for row in range(x+1, len(words)):
                if y < len(words[row]):
                    w2.append(words[row][y])
            if w1 != w2:
                return False
            x += 1
            y += 1
        return True