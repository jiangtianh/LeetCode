class Solution:
  
    def calculate(self, time):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return sum(days[:int(time.split('-')[0]) - 1]) + int(time.split('-')[1])

    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        alice = [self.calculate(arriveAlice), self.calculate(leaveAlice)]
        bob = [self.calculate(arriveBob), self.calculate(leaveBob)]
        if bob[0] <= alice[0] <= bob[1]:
            if bob[1] <= alice[1]:
                return bob[1] - alice[0] + 1
            else:
                return alice[1] - alice[0] + 1
        elif alice[0] <= bob[0] <= alice[1]:
            if alice[1] <= bob[1]:
                return alice[1] - bob[0] + 1
            else:
                return bob[1] - bob[0] + 1
        else:
            return 0

