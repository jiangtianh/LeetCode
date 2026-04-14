class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        robotCount = len(robot)
        
        factoryPositions = []
        for f in factory:
            factoryPositions.extend([f[0]] * f[1])
        factoryCount = len(factoryPositions)
        
        dp = [[None] * (factoryCount + 1) for _ in range(robotCount + 1)]
        
        def f(robotIdx, factoryIdx):
            if dp[robotIdx][factoryIdx]:
                return dp[robotIdx][factoryIdx]
            if robotIdx == robotCount:
                return 0
            elif factoryIdx == factoryCount:
                return math.inf

            assign = abs(factoryPositions[factoryIdx] - robot[robotIdx]) + f(robotIdx + 1, factoryIdx + 1)
            notAssign = f(robotIdx, factoryIdx + 1)

            res = min(assign, notAssign)
            dp[robotIdx][factoryIdx] = res

            return res

        return f(0, 0)

            