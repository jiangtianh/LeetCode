class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn > 8:
            return []
        self.temp = ["0"] * 10
        self.res = []


        def f(i, count):
            if count == turnedOn:
                self.res.append(self.temp[:])
                return
            for j in range(i, 10):
                self.temp[j] = "1"
                f(j + 1, count + 1)
                self.temp[j] = "0"
        
        f(0, 0)

        def toVal(li):
            hours = int("".join(li[:4]), 2)
            minutes = int("".join(li[4:]), 2)
            return hours, minutes

        res = []
        for i in range(len(self.res)-1, -1, -1):
            hours, minutes = toVal(self.res[i])
            if hours >= 12 or minutes >= 60:
                continue
            hours = str(hours)
            minutes = str(minutes)
            if len(minutes) == 1:
                minutes = "0" + minutes
            res.append(hours + ":" + minutes)

        
        return res