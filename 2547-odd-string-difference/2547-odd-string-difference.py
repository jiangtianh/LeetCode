class Solution:
    def oddString(self, words: List[str]) -> str:
        diff = []
        n = len(words[0])

        for word in words:
            temp = []
            for j in range(n-1):
                temp.append(ord(word[j+1]) - ord(word[j]))
            diff.append(temp)
        
        print(diff)

        
        other = None
        count = 1
        for i in range(1, len(diff)):
            if diff[i] == diff[0]:
                count += 1
            else:
                other = i
        if count == 1:
            return words[0]
        else:
            return words[other]