class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        Dx, Dy = 0, 1
        obst = set()
        for x, y in obstacles:
            obst.add((x, y))

        def process(command):
            nonlocal Dx, Dy, x, y
            if command == -2:
                if Dx == 0:
                    if Dy == 1:
                        Dy = 0
                        Dx = -1
                    else:
                        Dx = 1
                        Dy = 0
                elif Dy == 0:
                    if Dx == 1:
                        Dx = 0
                        Dy = 1
                    else:
                        Dx = 0
                        Dy = -1

            elif command == -1:
                if Dx == 0:
                    if Dy == 1:
                        Dx = 1
                        Dy = 0
                    else:
                        Dx = -1
                        Dy = 0
                elif Dy == 0:
                    if Dx == 1:
                        Dx = 0
                        Dy = -1
                    else:
                        Dx = 0
                        Dy = 1

            else:
                obs = False
                testX, testY = x, y
                for _ in range(command):
                    testX += Dx
                    testY += Dy
                    if (testX, testY) in obst:
                        obs = True
                        break
                    x = testX
                    y = testY
            
        res = 0
        x, y = 0, 0
        for command in commands:
            process(command)
            res = max(res, x ** 2 + y ** 2)
        return res
        