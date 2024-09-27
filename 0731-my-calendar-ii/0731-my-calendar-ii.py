class MyCalendarTwo:

    def __init__(self):
        self.singleBooking = []
        self.doubleBooking = []

    def book(self, start: int, end: int) -> bool:
        
        for i, j in self.doubleBooking:
            
            if start < j and end > i:
                return False 
            
        for i, j in self.singleBooking:
            if start < j and end > i:
                self.doubleBooking.append((max(start, i), min(end, j)))
                
        self.singleBooking.append((start, end))
        
        return True