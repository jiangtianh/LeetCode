class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordListSet = set(wordList)
        if endWord not in wordListSet or beginWord == endWord:
            return 0

        availableC = set() 
        for word in wordList:
            for c in word:
                availableC.add(c)

        def changeC(s, i, c):
            return s[:i] + c + s[i+1:]
        
        seen = {beginWord}
        q = collections.deque()
        q.append(beginWord)
        count = 1
        length = len(beginWord)

        while q:
            count += 1
            for _ in range(len(q)):
                curWord = q.popleft()

                for i in range(length):
                    for c in availableC:
                        newWord = changeC(curWord, i, c)
                        if newWord == endWord:
                            return count
                        if newWord not in seen and newWord in wordListSet:
                            seen.add(newWord)
                            q.append(newWord)
        
        return 0
        



