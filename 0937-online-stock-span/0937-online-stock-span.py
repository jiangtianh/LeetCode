class StockSpanner:

    def __init__(self):
        self.prices = []
        self.stack = []
        

    def next(self, price: int) -> int:
        

        i = len(self.prices) - 1

        if not self.stack or self.prices[i] > price:
            self.stack.append(1)
            self.prices.append(price)
            return 1
        else:
            res = 1
            while i >= 0 and self.prices[i] <= price:
                step = self.stack[i]
                res += step
                i -= step
            self.stack.append(res)
            self.prices.append(price)
            return res
            



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)