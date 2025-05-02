class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        indexes = []
        
        for i, direction in enumerate(dominoes):
            if direction != ".":
                indexes.append([i, direction])
        
        if len(indexes) == 0:
            return dominoes
        

        def f(l, r):
            leftIdx, leftDirection = l
            rightIdx, rightDirection = r
            elementBetween = rightIdx - leftIdx - 1
            if leftDirection == rightDirection:
                return [leftDirection for _ in range(elementBetween)]
            else:
                if leftDirection == "L" and rightDirection == "R":
                    return ["." for _ in range(elementBetween)]
                else:
                    half = elementBetween // 2
                    if elementBetween % 2 == 0:
                        return ["R"] * half + ["L"] * half
                    else:
                        return ["R"] * half + ["."] + ["L"] * half

        res = []
        for i in range(len(indexes) - 1):
            res.append(indexes[i][1])
            res.extend(f(indexes[i], indexes[i+1]))
        
        res.append(indexes[-1][1])
        if indexes[0][1] == "L":
            res = ["L"] * indexes[0][0] + res
        else:
            res = ["."] * indexes[0][0] + res
        if indexes[-1][1] == "R":
            res += ["R"] * (len(dominoes) - indexes[-1][0] - 1)
        else:
            res += ["."] * (len(dominoes) - indexes[-1][0] - 1)
        
        return "".join(res)

        