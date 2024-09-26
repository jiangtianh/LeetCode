class MyCalendar:

    def __init__(self):
        self.li = []
                

    def book(self, start: int, end: int) -> bool:
        if not self.li:
            self.li.append([start, end])
            return True 

        l = 0
        r = len(self.li) - 1

        while l <= r:
            m = (l + r) // 2
            if self.li[m][1] > start:
                r = m - 1
            else:
                l = m + 1
        
        if l >= len(self.li):
            self.li.append([start, end])
            return True 
        elif l == 0:
            if self.li[l][0] >= end:
                self.li.insert(0, [start, end])
                return True
        elif self.li[l][0] >= end and self.li[l-1][1] <= start:
            self.li.insert(l, [start, end])
            return True


        return False



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)