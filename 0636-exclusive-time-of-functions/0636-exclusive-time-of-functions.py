class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        d = [0] * n
        lastTime = 0

        for log in logs:
            ID, operation, time = log.split(":")
            ID, time = int(ID), int(time)

            if operation == "start":
                if stack:
                    d[stack[-1]] += time - lastTime
                stack.append(ID)
                lastTime = time
            else:
                d[stack.pop()] += time - lastTime + 1
                lastTime = time + 1
        return d    



