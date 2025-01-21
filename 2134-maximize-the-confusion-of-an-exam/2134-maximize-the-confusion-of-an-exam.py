class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        l = 0
        res = 0
        TCount = 0
        FCount = 0

        for r in range(len(answerKey)):
            answer = answerKey[r]
            
            if answer == "T":
                TCount += 1
            else:
                FCount += 1
            
            while min(TCount, FCount) > k:
                lanswer = answerKey[l]
                if lanswer == "T":
                    TCount -= 1
                else:
                    FCount -= 1
                l += 1
            res = max(res, r - l + 1)
        return res