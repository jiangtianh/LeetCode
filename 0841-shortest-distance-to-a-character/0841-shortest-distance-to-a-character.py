class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        cIdx = []
        for i, char in enumerate(s):
            if char == c:
                cIdx.append(i)

        idx = 0
        res = [0] * len(s)

        for i, char in enumerate(s):
            if i > cIdx[idx]:
                if idx + 1 < len(cIdx) and cIdx[idx+1] - i < abs(i - cIdx[idx]):
                    idx += 1
            res[i] = abs(cIdx[idx] - i)

        return res