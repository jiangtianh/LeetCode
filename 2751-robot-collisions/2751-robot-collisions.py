class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        N = len(positions)
        li = [[positions[i], healths[i], directions[i], i] for i in range(N)]
        original = li[:]

        li.sort(key=lambda x: x[0])
        stack = []

        for position, health, direction, i in li:
            if not stack:
                stack.append([health, direction, i])
            else:
                if direction == "L":
                    flag = False
                    while stack and stack[-1][1] == "R":
                        if stack[-1][0] == health:
                            stack.pop()
                            flag = True
                            break
                        elif stack[-1][0] < health:
                            stack.pop()
                            health -= 1
                        else:
                            stack[-1][0] -= 1
                            flag = True
                            break
                    if not flag:
                        stack.append([health, direction, i])
                else:
                    stack.append([health, direction, i])

        d = {}
        for h, di, i in stack:
            d[i] = h
        
        res = []
        for i in range(N):
            if i in d:
                res.append(d[i])
        return res
                    